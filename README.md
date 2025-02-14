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
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the script**:
   ```bash
   python investment_decision.py
   ```

## Data Downloading

The `investment_decision.py` script includes functionality to download historical stock data using the [yfinance](https://pypi.org/project/yfinance/) library. When you run the script, you'll be prompted to enter a ticker symbol (for example, `AAPL`). The script then downloads 5 years of historical data for that ticker and displays the first 5 rows as confirmation.

### Key Code Snippet:

```python
def download_data():
    ticker = input("Enter the ticker symbol (e.g., AAPL): ").strip().upper()
    print(f"Downloading data for {ticker}...")
    data = yf.download(ticker, period="5y", interval="1d")
    
    if data.empty:
        print("No data found. Please check the ticker symbol and try again.")
        return None

    print("Data downloaded successfully. Here are the first 5 rows:")
    print(data.head())
    
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)  # Flatten MultiIndex
    
    data.reset_index(inplace=True)
    return data
```

## Technical Indicators Computed

The script computes key technical indicators to help analyze stock trends:

1. **SMA50 (50-day Simple Moving Average)** - Calculates the average closing price over the last 50 days.
2. **SMA200 (200-day Simple Moving Average)** - Calculates the average closing price over the last 200 days.
3. **RSI (Relative Strength Index)** - Measures momentum and identifies potential overbought or oversold conditions.

### Technical Indicators Calculation Snippet:

```python
def compute_indicators(data):
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
```

## Example Output

When the script is run and a valid ticker is provided, it displays:

```
Welcome to the Investment Decision Project!
Enter the ticker symbol (e.g., AAPL): AAPL
Downloading data for AAPL...
[*********************100%***********************]  1 of 1 completed
Data downloaded successfully. Here are the first 5 rows:

    Close    SMA50      SMA200      RSI
0   150.25   149.98     148.34     45.23
1   151.10   150.32     148.67     48.12
2   152.20   150.78     149.01     52.87
3   153.15   151.20     149.42     56.34
4   154.00   151.65     149.80     60.11
```

## Future Enhancements

- **Add MACD (Moving Average Convergence Divergence) indicator**
- **Implement Bollinger Bands**
- **Improve visualization using Matplotlib or Plotly**
- **Generate buy/sell recommendations based on RSI & SMA crossovers**

