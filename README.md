# Cointegration Dickey Fuller Tester (financial app)

The deployed version is available here : https://gamaiun-stocks-cointegration-app3-ws8v9m.streamlit.app/

The idea behind cointegration models is that even if the prices of two different assets both follow a random walk, it is still possible that a linear combination of these assets is not a random walk. Thus, even if asset A and B are not forecastable, there is a possibility that the linear combination of these assets is (forecastable). In such a case, we say that the assets A and B are cointegrated. To test the cointegration of two assets we first regress asset Pt over the asset Qt to get the slope C. We then run an augmented Dickey-Fuller test on Pt-CQt to test for random walk.

Example: 
Passing NOG (Northern Oil and Gas Inc) and PBF (PBF Energy Inc. Refines petroleum and sells transportation fuels, lubricants, heating oil, and feedstocks) results in p_value of 0.019 in Dickey Fuller test, providing strong evidence of cointegration between the two stocks. 
