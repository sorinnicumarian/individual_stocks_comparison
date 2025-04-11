import os
import pandas as pd
import finnhub
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Finnhub client
finnhub_client = finnhub.Client(api_key=os.getenv('FINNHUB_API_KEY'))

# Define the list of company symbols (you can add more if needed)
companies = [
    {'name': 'Apple', 'symbol': 'AAPL'},
    {'name': 'Equifax', 'symbol': 'EFX'},
    {'name': 'Alphabet', 'symbol': 'GOOGL'},
    {'name': 'Nvidia', 'symbol': 'NVDA'},
    {'name': 'Procter & Gamble', 'symbol': 'PG'},
    {'name': 'Tesla', 'symbol': 'TSLA'},
    {'name': 'Microsoft', 'symbol': 'MSFT'},
    {'name': 'Oracle', 'symbol': 'ORCL'}
]

# Function to fetch data for each company
def get_stock_data(symbol):
    try:
        # Get quote data (current price, market cap, PE ratio, etc.)
        quote = finnhub_client.quote(symbol)
        
        # Get company profile (for company name and other details)
        profile = finnhub_client.company_profile2(symbol=symbol)

        # Get company basic financials (e.g., income statement)
        financials = finnhub_client.company_basic_financials(symbol=symbol, metric='income_statement')

        # Extract relevant data
        data = {
            'Company Name': profile.get('name', 'N/A'),
            'Symbol': symbol,
            'Current Price': quote.get('c', 'N/A'),
            'Market Cap (Intraday)': quote.get('m', 'N/A'),
            'PE Ratio (TTM)': financials.get('pe', 'N/A'),  # Example for PE ratio
            'P/B Ratio': financials.get('pb', 'N/A'),  # P/B ratio might be available here
            'ROE': financials.get('roe', 'N/A'),  # ROE (Return on Equity)
            'Dividend Yield': financials.get('dividend_yield', 'N/A')  # Dividend yield
        }
        return data
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

# Fetch data for all companies
company_data = []
for company in companies:
    data = get_stock_data(company['symbol'])
    if data:
        company_data.append(data)

# Convert the data into a pandas DataFrame
df = pd.DataFrame(company_data)

# Display the data
print(df)