import pandas as pd
from dotenv import load_dotenv
import os
import sqlalchemy
from sqlalchemy import inspect
import csv
import time
import FMP_Requests as fmp

load_dotenv()
apikey = os.getenv("FMP_API_KEY")

# Create a SQLite database and populate the database with content from the stocks_data.db file
database_connection_string = 'sqlite:///stocks_data.db'

# Create an engine to interact with the SQLite database
engine = sqlalchemy.create_engine(database_connection_string)

# Show tables in the SQLite database.
engine.table_names()


# import S&P500 tickers from fmp_sp500.csv
with open('fmp_sp500.csv', 'r') as file:
    tickers = file.read().splitlines()

# tickers = ['AAPL']

# Get Income Statements for S&P 500 tickers and save each income statement into database
i = 1
for ticker in tickers:

    response = fmp.get_income_statement(ticker, apikey)
    income_statement_df = pd.DataFrame(response)
    
    income_statement_df.to_sql(
        ticker+'_income_statment', 
        engine, 
        index=True, 
        if_exists='replace'
    )
    print(i, " Downloaded Income Statement for " + ticker)
    i = i + 1
    time.sleep(0.3)


# Process Income Statements
# Create a SQLite database and populate the database with content from the stocks_data.db file
database_connection_string2 = 'sqlite:///stocks_data_processed.db'

# Create an engine to interact with the SQLite database
engine2 = sqlalchemy.create_engine(database_connection_string2)

i = 1
for ticker in tickers:

    query = "SELECT * from " + ticker + "_income_statment"
#   query = "SELECT * from BOAPL_income_statment"
    print (query)
    df = pd.read_sql_query(query, con=engine)
    df = df.T
    df.columns = df.loc['calendarYear'] 
    
    df.to_sql(
        ticker+'_income_statment_processed', 
        engine2, 
        index=True, 
        if_exists='replace'
    )
    print(i, " Processed Income Statemet for " + ticker)
    i = i + 1

# Confirm that the table was created by calling the table_names function
engine2.table_names()

# Get Key Metrics for S&P 500 tickers and save each key metrics into database
i = 1
for ticker in tickers:

    response = fmp.get_key_metrics(ticker, apikey)
    df = pd.DataFrame(response)
    
    df.to_sql(
        ticker+'_key_metrics', 
        engine, 
        index=True, 
        if_exists='replace'
    )
    print(i, " Downloaded " + ticker)
    i = i + 1
    time.sleep(0.3)


# Process Key Metrics
# Create a SQLite database - stocks_data_processed.db file
database_connection_string2 = 'sqlite:///stocks_data_processed.db'

# Create an engine to interact with the SQLite database
engine2 = sqlalchemy.create_engine(database_connection_string2)

i = 1
for ticker in tickers:

    query = "SELECT * from " + ticker + "_key_metrics"
    print (query)
    df = pd.read_sql_query(query, con=engine)
    cols = df['date'].str[:4]
    df = df.T
    df.columns = cols
    
    df.to_sql(
        ticker+'_key_metrics_processed', 
        engine2, 
        index=True, 
        if_exists='replace'
    )
    print(i, " Processed Key Metrics for " + ticker)
    i = i + 1

"""

print (tickers)

response = fmp.get_sp500_constituent(apikey)
df = pd.DataFrame(response)
df.to_csv('fmp_sp500.csv')

query = "SELECT * from ZTS_income_statment_processed"
df3 = pd.read_sql_query(query, con=engine2)

engine.execute("DROP TABLE KO_income_statment")

inspector = inspect(engine)
print(inspector.get_table_names())

"""


