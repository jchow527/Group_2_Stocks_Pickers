import pandas as pd
import os
import requests
import json
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from MCForecastTools import MCSimulation
import datetime
from dateutil.relativedelta import relativedelta
import portfolio_builder_calc_ranking as cr
import FMP_Requests as fmp


# Load the environment variables from the .env file
load_dotenv()
apikey = os.getenv("FMP_API_KEY")

year = "2015"

# get ranking for given year by using portfolio_builder_calc_ranking module
df = cr.get_ranking(year)

# get top 5 companies from dataframe df
top5_df = df.head(n=5)
top5_tickers_list = list(top5_df.index)


# get past stock prices of top 5 companies and store in stock_prices dictionary
start_date = year + "-01-15"
end_date = year + "-01-20"
past_stock_prices = {}
for ticker in top5_tickers_list:

    prices = fmp.get_stock_hist_daily_prices(ticker, start_date, end_date, apikey)
    price = prices['close'].iloc[-1]
    past_stock_prices[ticker] = price
    
past_stock_prices_df = pd.DataFrame.from_dict(past_stock_prices, orient="index")
past_stock_prices_df.columns = ['past_price']
    
 
# get current stock prices of top 5 companies and store in stock_prices dictionary
current_stock_prices = {}
for ticker in top5_tickers_list:
    
    prices = fmp.get_current_stock_price(ticker, apikey)
    price_df = pd.DataFrame(prices)
    price = price_df.iloc[0,1]
    current_stock_prices[ticker] = price 
    
current_stock_prices_df = pd.DataFrame.from_dict(current_stock_prices, orient="index")
current_stock_prices_df.columns = ['current_price']

price_change_df = pd.concat([current_stock_prices_df, past_stock_prices_df], axis=1)
price_change_df['price_change'] = current_stock_prices_df['current_price'] - past_stock_prices_df['past_price']
print("Past Price is based on Jan " + year)
print ("Current Price is last working day close price")
print()
print(price_change_df)

