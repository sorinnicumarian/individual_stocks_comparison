import yfinance as yf
import pandas as pd
from pandas_profiling import ProfileReport
import time
import numpy as np

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
# Save your DataFrame as CSV
df.to_csv('stocks_data.csv', index=False)  # Set index=False to avoid saving the index column

# Assign weights for classification
weights = {
    'PE Ratio (TTM)': 0.25,
    'P/B Ratio': 0.25,
    'ROE': 0.25,
    'Dividend Yield': 0.25
}

# Function to classify stocks based on parameters
def classify_stock(row):
    classification_values = {'Undervalued': 1, 'Normal Valued': 0, 'Overvalued': -1}

    # Classify based on PE Ratio
    if row['PE Ratio (TTM)'] < 8:
        pe_category = 'Undervalued'
    elif 8 <= row['PE Ratio (TTM)'] <= 15:
        pe_category = 'Normal Valued'
    else:
        pe_category = 'Overvalued'

    # Classify based on P/B Ratio
    if row['P/B Ratio'] and row['P/B Ratio'] < 1:
        pb_category = 'Undervalued'
    elif row['P/B Ratio'] and 1 <= row['P/B Ratio'] <= 3:
        pb_category = 'Normal Valued'
    else:
        pb_category = 'Overvalued'
    
    # Classify based on ROE
    if row['ROE'] and row['ROE'] > 12:
        roe_category = 'Undervalued'
    elif row['ROE'] and 8 <= row['ROE'] <= 12:
        roe_category = 'Normal Valued'
    else:
        roe_category = 'Overvalued'
    
    # Classify based on Dividend Yield
    if row['Dividend Yield'] and row['Dividend Yield'] > 3.5:
        dividend_category = 'Undervalued'
    elif row['Dividend Yield'] and 2 <= row['Dividend Yield'] <= 3.5:
        dividend_category = 'Normal Valued'
    else:
        dividend_category = 'Overvalued'

    # Calculate weighted average for stock classification
    categories = [pe_category, pb_category, roe_category, dividend_category]
    weighted_average = np.average([classification_values[cat] for cat in categories], weights=[weights['PE Ratio (TTM)'], weights['P/B Ratio'], weights['ROE'], weights['Dividend Yield']])

    # Return the classification of the stock based on weighted average
    if weighted_average >= 0.6:
        final_category = 'Undervalued'
    elif weighted_average <= -0.4:
        final_category = 'Overvalued'
    else:
        final_category = 'Normal Valued'

    return pe_category, pb_category, roe_category, dividend_category, final_category

# Apply classification to each stock and calculate weighted average
df[['PE Category', 'PB Category', 'ROE Category', 'Dividend Category', 'Overall Category']] = df.apply(classify_stock, axis=1, result_type='expand')

# Function to apply conditional formatting based on category
def apply_color(s):
    color_map = {
        'Undervalued': 'background-color: lightgreen',
        'Normal Valued': 'background-color: lightyellow',
        'Overvalued': 'background-color: lightcoral'
    }
    return s.map(color_map)

# Apply conditional formatting to columns
styled_df = df.style.applymap(apply_color, subset=['PE Category', 'PB Category', 'ROE Category', 'Dividend Category'])

# Print the dataframe with conditional formatting

# Generate the report
profile = ProfileReport(styled_df, title="Stocks Data Profiling Report", explorative=True)

# Save the report as an HTML file
profile.to_file("stocks_data_report.html")