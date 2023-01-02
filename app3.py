import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import sys, os 
import requests
import datetime
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import plotly.offline as pyo
from plotly.subplots import make_subplots
from scipy.stats import skew, kurtosis
from statsmodels.tsa.stattools import adfuller

import os

import dash 
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash_bootstrap_components._components.Container import Container
import plotly.express as px
import altair as alt
import matplotlib.pyplot as plt
import plotly.graph_objects as go


# Sidebar
st.set_page_config(layout="wide")

st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 2rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 2rem;
                    padding-right: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

# st.markdown("""
#         <style>
#                .css-18e3th9 {
#                     padding-top: 0rem;
#                     padding-bottom: 0rem;
#                     padding-left: 5rem;
#                     padding-right: 5rem;
#                 }
#                .css-1d391kg {
#                     padding-top: 0rem;
#                     padding-right: 1rem;
#                     padding-bottom: 0rem;
#                     padding-left: 1rem;
#                 }
#         </style>
#         """, unsafe_allow_html=True)

# st.markdown(    
#     """
#     <style>
#     [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
#         width: 500px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,)

#################### Sidebar ######################


import time

today = datetime.date.today()
with st.sidebar:

    start_date = st.date_input(label = "FROM", value=pd.to_datetime("2015-01-31", format="%Y-%m-%d"))
    end_date = st.date_input(label = "TO", value = today)

    stock1 = st.text_input(f'Enter stock N1', value = "NOG")
    stock2 = st.text_input(f'Enter stock N', value = "AAPL")
    
    with st.expander("Cointegration. See explanation"):
        st.write(" The idea behind cointegration models is that even if the prices of two different \
            assets both follow a *random walk*, it is still possible that a linear combination of these assets \
            is not a *random walk*. Thus, even if asset A and B are not forecastable, there is a possibility that\
            the linear combination of these assets is (forecastable). In such a case, we say that the assets A and B are *cointegrated*.\
            To test the cointegration of two assets we first regress asset *Pt* over the asset *Qt* to get the slope *C*.\
            We then run an augmented Dickey-Fuller test on *Pt-CQt* to test for *random walk*.")
        #st.image("https://static.streamlit.io/examples/dice.jpg")


       # weights["w_{}".format(i)] = st.text_input(f"Enter portfolio weight N{i+1}")
stock_1 = yf.download(stock1, start = start_date, end = end_date)
stock_2 = yf.download(stock2, start = start_date, end = end_date)

adfuller_result_1 = adfuller(stock_1["Close"])
adfuller_result_2 = adfuller(stock_2["Close"])

st.subheader(f"Testing {stock1} and {stock2} using Dickey-Fuller test:")
st.write(f"Stock {stock1} Dickey-Fuller test p_value is ", adfuller_result_1[1])
if adfuller_result_1[1] < 0.05:
    st.write(f"We found evidence to reject the null hypothesis that the {stock1} follows a random walk")
else:
    st.write(f"We found no evidence to reject the null hypothesis that the {stock1} follows a random walk")

st.write("----")

st.write(f"Stock {stock2} Dickey-Fuller test p_value is ", adfuller_result_2[1])
if adfuller_result_2[1] < 0.05:
    st.write(f"We found evidence to reject the null hypothesis that the {stock2} follows a random walk")
else:
    st.write(f"We found no evidence to reject the null hypothesis that the {stock2} follows a random walk")
st.write("----")

st.subheader(f"Testing cointegration of {stock1} and {stock2}")
adfuller_spread = adfuller(stock_1["Close"] - stock_2["Close"])

st.write(f"Cointegration Dickey-Fuller test p_value is ", adfuller_spread[1])
if adfuller_spread[1] < 0.05:
    st.write(f"We found evidence to suggest that the stocks are cointegrated")
else:
    st.write(f"We found *no* evidence to suggest that the stocks are cointegrated")
st.write("----")



