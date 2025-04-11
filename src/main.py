import yfinance as yf
import pandas as pd
import time

# List of company symbols
symbols = ['AAPL', 'GOOGL', 'MSFT', 'TSLA']
stock_data = []

for symbol in symbols:
    try:
        # Fetch stock data using yfinance
        ticker = yf.Ticker(symbol)
        profile = ticker.info

        stock_data.append({
            'Company Name': profile.get('longName', 'N/A'),
            'Symbol': symbol,
            'Current Price': profile.get('currentPrice', 'N/A'),
            'Market Cap (Intraday)': profile.get('marketCap', 'N/A'),
            'PE Ratio (TTM)': profile.get('trailingPE', 'N/A'),
            'P/B Ratio': profile.get('priceToBook', 'N/A'),
            'ROE': profile.get('returnOnEquity', 'N/A'),
            'Dividend Yield': profile.get('dividendYield', 'N/A')
        })
        
        # Sleep between requests to avoid rate limiting
        time.sleep(1)  # Adjust based on your needs

    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        stock_data.append({
            'Company Name': 'N/A',
            'Symbol': symbol,
            'Current Price': 'N/A',
            'Market Cap (Intraday)': 'N/A',
            'PE Ratio (TTM)': 'N/A',
            'P/B Ratio': 'N/A',
            'ROE': 'N/A',
            'Dividend Yield': 'N/A'
        })

# Convert to DataFrame for better visualization
df = pd.DataFrame(stock_data)
print(df)