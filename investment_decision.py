import yfinance as yf
import pandas as pd


def download_data():
    ticker = input("Enter the ticker symbol (e.g., AAPL): ").strip().upper()
    print(f"Downloading data for {ticker}...")

    data = yf.download(ticker, period="2mo", interval="1d")

    if data.empty:
        print("No data found. Please check the ticker symbol and try again.")
        return None

    print("Data downloaded successfully. Here are the first 5 rows:")
    print(data.head())

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)  # Flatten MultiIndex

    data.reset_index(inplace=True)

    return data


def compute_indicators(data):

    # Computes key technical indicators: SMA50, SMA200, and RSI.

    if "Close" not in data.columns:
        print("Error: 'Close' column not found in data.")
        print("Available columns:", data.columns)
        return data

   
    data["SMA50"] = data["Close"].rolling(window=50, min_periods=1).mean()
    data["SMA200"] = data["Close"].rolling(window=200, min_periods=1).mean()

    
    delta = data["Close"].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=14, min_periods=1).mean()
    avg_loss = loss.rolling(window=14, min_periods=1).mean()

    rs = avg_gain / avg_loss
    data["RSI"] = 100 - (100 / (1 + rs))

    return data



def main():
    print("Welcome to the Investment Decision Project!")
    
    data = download_data()
    if data is None:
        return  # Stop if no data was downloaded
    
    
    data = compute_indicators(data)
    
    
    print("\nData with Technical Indicators:")
    print(data[['Close', 'SMA50', 'SMA200', 'RSI']].head())


    
if __name__ == "__main__":
    main()