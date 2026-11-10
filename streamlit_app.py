import streamlit as st
import yfinance as yf
import pandas as pd

# Title of the app
st.title("Microsoft (MSFT) Sharpe Ratio")
st.write("5-Year Monthly Sharpe Ratio for Microsoft")

# Define the ticker and monthly risk-free rate
ticker = "MSFT"
rf_monthly = 0.0025  # 0.25% per month

# Download 5 years of monthly stock data
data = yf.Ticker(ticker).history(period="5y", interval="1mo")

if not data.empty:
    # Get closing prices
    close_prices = data["Close"]

    # Calculate monthly returns
    monthly_returns = close_prices.pct_change().dropna()

    # Calculate excess returns
    excess_returns = monthly_returns - rf_monthly

    # Calculate average excess return and standard deviation
    mean_excess_return = excess_returns.mean()
    std_dev_return = monthly_returns.std()

    # Calculate Monthly Sharpe Ratio
    if pd.notna(std_dev_return) and std_dev_return > 0:
        monthly_sharpe_ratio = mean_excess_return / std_dev_return

        # Display results
        st.metric(
            label="Monthly Sharpe Ratio",
            value=f"{monthly_sharpe_ratio:.3f}"
        )

        st.write(f"Ticker: {ticker}")
        st.write("Period: 5 Years")
        st.write("Monthly Risk-Free Rate: 0.25%")
    else:
        st.error("Not enough return data to calculate the Sharpe Ratio.")
else:
    st.error("No data found for MSFT.")
