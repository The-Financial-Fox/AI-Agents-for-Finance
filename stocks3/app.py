#######################
# Import libraries
import streamlit as st
import pandas as pd
import yfinance as yf
import altair as alt
import plotly.graph_objects as go

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
    if not stock_data.empty:
        latest_close = stock_data['Close'].dropna().iloc[-1]
        if isinstance(latest_close, (float, int)):
            st.metric("Latest Close Price", f"${latest_close:.2f}")
        else:
            st.metric("Latest Close Price", "N/A")
    else:
        st.metric("Latest Close Price", "N/A")

with col2:
    if not stock_data.empty:
        highest_price = stock_data['High'].dropna().max()
        if isinstance(highest_price, (float, int)):
            st.metric("Highest Price", f"${highest_price:.2f}")
        else:
            st.metric("Highest Price", "N/A")
    else:
        st.metric("Highest Price", "N/A")

with col3:
    if not stock_data.empty:
        lowest_price = stock_data['Low'].dropna().min()
        if isinstance(lowest_price, (float, int)):
            st.metric("Lowest Price", f"${lowest_price:.2f}")
        else:
            st.metric("Lowest Price", "N/A")
    else:
        st.metric("Lowest Price", "N/A")

# Line Chart
if not stock_data.empty:
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
    candlestick_fig = go.Figure(data=[
        go.Candlestick(
            x=stock_data['Date'],
            open=stock_data['Open'],
            high=stock_data['High'],
            low=stock_data['Low'],
            close=stock_data['Close']
        )
    ])
    candlestick_fig.update_layout(
        title=f"{selected_ticker} Candlestick Chart",
        xaxis_title="Date",
        yaxis_title="Price ($)",
        template="plotly_dark",
        height=600
    )
    st.plotly_chart(candlestick_fig, use_container_width=True)
else:
    st.write("No data available for the selected ticker and date range.")

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
    st.sidebar.write("Developed with ❤️ by [Christian Martinez and ChatGPT")
