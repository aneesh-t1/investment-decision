import yfinance as yf
import pandas as pd


def download_data():
    ticker = input("Enter the ticker symbol (e.g., AAPL): ").strip().upper()
    print(f"Downloading data for {ticker}...")
    data = yf.download(ticker, period = "5y")

    if data.empty:
        print("No data found. Please check the ticker symbol and try again.")
        return None

    print("Data downloaded successfully. Here are the first 5 rows:")
    print(data.head())
    return data


def main():
    print("Welcome to the Investment Decision Project!")

    download_data()

    
if __name__ == "__main__":
    main()