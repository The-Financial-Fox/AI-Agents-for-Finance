import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from pptx import Presentation
from pptx.util import Inches
import pandas as pd
import io

def fetch_stock_data(ticker, period='1y'):
    """Fetch stock data using yfinance."""
    stock = yf.Ticker(ticker)
    return stock.history(period=period)

def create_visualizations(data, ticker):
    """Create and return stock data visualizations."""
    plots = {}
    # Closing Price Plot
    plt.figure(figsize=(10, 5))
    plt.plot(data['Close'], label='Close Price')
    plt.title(f'{ticker} Closing Prices')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plots['Closing Prices'] = buf
    plt.close()

    # Volume Plot
    plt.figure(figsize=(10, 5))
    plt.bar(data.index, data['Volume'], color='orange')
    plt.title(f'{ticker} Volume')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plots['Volume'] = buf
    plt.close()

    return plots

def create_powerpoint(plots, ticker):
    """Create a PowerPoint presentation with stock data visualizations."""
    prs = Presentation()

    # Title Slide
    slide = prs.slides.add_slide(prs.slide_layouts[0])
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    title.text = f"Stock Analysis for {ticker}"
    subtitle.text = "Generated using yfinance and Streamlit"

    # Add slides for each plot
    for title, plot in plots.items():
        slide = prs.slides.add_slide(prs.slide_layouts[5])
        title_placeholder = slide.placeholders[0]
        title_placeholder.text = title

        # Add the plot image
        img_path = plot
        img = slide.shapes.add_picture(img_path, Inches(1), Inches(1.5), width=Inches(8))

    # Save PowerPoint to BytesIO
    ppt_io = io.BytesIO()
    prs.save(ppt_io)
    ppt_io.seek(0)
    return ppt_io

# Streamlit App
def main():
    st.title("Stock Analysis and PowerPoint Generator")

    st.sidebar.header("User Input")
    stocks = st.sidebar.text_input("Enter stock tickers (comma-separated):", "AAPL, MSFT")
    period = st.sidebar.selectbox("Select the period for data:", ['1mo', '3mo', '6mo', '1y', '2y', '5y'], index=3)

    if st.sidebar.button("Generate Report"):
        tickers = [ticker.strip() for ticker in stocks.split(",")]
        ppt_files = {}

        for ticker in tickers:
            st.write(f"Fetching data for {ticker}...")
            try:
                data = fetch_stock_data(ticker, period)
                plots = create_visualizations(data, ticker)
                ppt_files[ticker] = create_powerpoint(plots, ticker)
                st.success(f"Data and visualizations for {ticker} prepared!")

                # Show visualizations
                for title, plot in plots.items():
                    st.image(plot, caption=f"{ticker} - {title}")

            except Exception as e:
                st.error(f"Error fetching data for {ticker}: {e}")

        if ppt_files:
            for ticker, ppt_file in ppt_files.items():
                st.download_button(
                    label=f"Download {ticker} Report", 
                    data=ppt_file, 
                    file_name=f"{ticker}_report.pptx", 
                    mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
                )

if __name__ == "__main__":
    main()
