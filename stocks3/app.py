#######################
# Import libraries
import streamlit as st
import pandas as pd
import yfinance as yf
import altair as alt
import plotly.express as px

#######################
# Page configuration
st.set_page_config(
    page_title="Stock Market Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

#######################
# Sidebar
st.sidebar.title('📈 Stock Market Dashboard')

def get_stock_data(ticker, start, end):
    stock_data = yf.download(ticker, start=start, end=end)
    stock_data.reset_index(inplace=True)
    return stock_data

# Inputs
selected_ticker = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, MSFT):", "AAPL")
start_date = st.sidebar.date_input("Start Date:", pd.to_datetime("2022-01-01"))
end_date = st.sidebar.date_input("End Date:", pd.to_datetime("2023-01-01"))

# Load Data
data_load_state = st.sidebar.text("Loading data...")
stock_data = get_stock_data(selected_ticker, start_date, end_date)
data_load_state.text("Data loaded successfully!")

#######################
# Main Panel
st.title(f"Stock Market Analysis: {selected_ticker}")
st.write(f"Analyzing data from {start_date} to {end_date}.")

# Display Raw Data
if st.checkbox("Show Raw Data"):
    st.write(stock_data)

# Key Metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Latest Close Price", f"${stock_data['Close'].iloc[-1]:.2f}")
with col2:
    st.metric("Highest Price", f"${stock_data['High'].max():.2f}")
with col3:
    st.metric("Lowest Price", f"${stock_data['Low'].min():.2f}")

# Line Chart
st.markdown('### Closing Price Over Time')
closing_chart = alt.Chart(stock_data).mark_line().encode(
    x='Date:T',
    y=alt.Y('Close:Q', title="Closing Price ($)"),
    tooltip=['Date:T', 'Close:Q']
).properties(width=800, height=400)
st.altair_chart(closing_chart, use_container_width=True)

# Volume Bar Chart
st.markdown('### Trading Volume')
volume_chart = alt.Chart(stock_data).mark_bar().encode(
    x='Date:T',
    y=alt.Y('Volume:Q', title="Volume"),
    tooltip=['Date:T', 'Volume:Q']
).properties(width=800, height=200)
st.altair_chart(volume_chart, use_container_width=True)

# Candlestick Chart
st.markdown('### Candlestick Chart')
candlestick_fig = px.line(stock_data, x="Date", y=["Open", "High", "Low", "Close"], 
                           labels={"value": "Price ($)", "variable": "Stock Price"},
                           title=f"{selected_ticker} Candlestick Chart")
st.plotly_chart(candlestick_fig, use_container_width=True)

#######################
# About Section
with st.expander("About this App", expanded=True):
    st.write('''
    - Data Source: Yahoo Finance (via [yfinance](https://github.com/ranaroussi/yfinance))
    - Use the sidebar to input stock ticker and date range.
    - Visualizations:
        - Line Chart: Closing price trends.
        - Bar Chart: Daily trading volume.
        - Candlestick Chart: Open, High, Low, Close price dynamics.
    ''')

#######################
# Run the App
if __name__ == "__main__":
    st.sidebar.write("Developed with ❤️ by [Christian Martinez and ChatGPT]")