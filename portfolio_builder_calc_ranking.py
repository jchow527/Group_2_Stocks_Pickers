### rank the companies by certain metrics.
### this is the module to modify to change the formula for choosing companies to include in a portfolio

import pandas as pd
import numpy as np
import portfolio_builder_get_year_data as gy


def get_ranking(year):
    
    # get the key metrics data for all companies by calling the get_year_data function in portfolio_builder_get_year_data.py
    df = gy.get_year_data(year)
    
    # df = df[df['dividend_yield']>0]
    
    # in dataframe df1, the original dataframe is ranked by earnings_yield
    df1 = df.sort_values(by='earnings_yield', ascending=False)
    df1['rank_num1'] = np.arange(len(df1))
    df1.set_index('ticker', inplace=True)

    # in dataframe df2, the original dataframe is ranked by return_on_tangible assets
    df2 = df.sort_values(by='return_on_tangible_assets', ascending=False)
    df2['rank_num2'] = np.arange(len(df2))
    df2.set_index('ticker', inplace=True)
    df2 = df2['rank_num2']

    # merge dataframes df1 and df2 into new dataframe df3
    df3 = pd.concat([df1, df2], axis=1)

    # sum the rankings of earning_yields and return_on_tangible assets for each ticker
    df3['rank_sum'] = df3['rank_num1'] + df3['rank_num2']

    # sort the sum of the rankings
    df3.sort_values('rank_sum', inplace=True)
    df3['rank'] = np.arange(len(df3))

    return df3


