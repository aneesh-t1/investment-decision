# Investment Decision Project

## Project Overview

This project analyzes historical stock data to compute technical indicators such as Simple Moving Averages (SMA) and the Relative Strength Index (RSI). Based on these indicators, it provides a simple recommendation on whether to invest in a stock and suggests a potential holding period.

## Technologies Used

- **Python**: Programming language used for analysis.
- **yfinance**: Library to fetch historical stock data.
- **pandas**: Data manipulation and analysis.
- **numpy**: Numerical operations.
- **matplotlib**: Data visualization.

## How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/investment-decision.git
   cd investment-decision

## Data Downloading

The `investment_decision.py` script now includes functionality to download historical stock data using the [yfinance](https://pypi.org/project/yfinance/) library. When you run the script, you'll be prompted to enter a ticker symbol (for example, `AAPL`). The script then downloads 5 years of historical data for that ticker and displays the first 5 rows as confirmation.

### Key Code Snippet:

```python
def download_data():
    ticker = input("Enter the ticker symbol (e.g., AAPL): ").strip().upper()
    print(f"Downloading data for {ticker}...")
    data = yf.download(ticker, period="5y")
    
    if data.empty:
        print("No data found. Please check the ticker symbol and try again.")
        return None