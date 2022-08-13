## Pull specific key metrics of a company by year

import pandas as pd
import sqlalchemy
from sqlalchemy import inspect
import csv

def get_year_data(year):
    # Create a SQLite database and populate the database with content from the stocks_data.db file
    database_connection_string = 'sqlite:///stocks_data_processed.db'
    
    # Create an engine to interact with the SQLite database
    engine = sqlalchemy.create_engine(database_connection_string)
    
    # Show tables in the SQLite database.
#    inspector = inspect(engine)
#    print(inspector.get_table_names())
    
    # import S&P500 tickers from fmp_sp500.csv
    with open('fmp_sp500.csv', 'r') as file:
        tickers = file.read().splitlines()

    dictionary = {}
    results_df = pd.DataFrame(dictionary)
    
    # pull key metrics for a specific year from the database
    for ticker in tickers:
        
        query = "SELECT * from " + ticker + "_key_metrics_processed"
        df = pd.read_sql_query(query, con=engine)
        df = df.fillna(0)
        
        
        # pick only selected metrics to form a new results_df dataframe, to improve speed of processing later
        if set([year]).issubset(df.columns):
            market_cap = float(df.loc[13,year])
            enterprise_value = float(df.loc[14,year])
            pe_ratio = float(df.loc[15,year])
            earnings_yield = float(df.loc[25, year])
            dividend_yield = float(df.loc[33, year])
            return_on_tangible_assets = float(df.loc[44,year])
            
            for variable in ["ticker", "market_cap", "enterprise_value", "pe_ratio", "earnings_yield", "dividend_yield", "return_on_tangible_assets"]:
                dictionary[variable] = eval(variable)
                
            results_df = results_df.append(dictionary, ignore_index=True)
            
    return results_df
    

