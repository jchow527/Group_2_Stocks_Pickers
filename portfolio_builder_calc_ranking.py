import pandas as pd
import numpy as np
import portfolio_builder_get_year_data as gy


def get_ranking(year):
    
    df = gy.get_year_data(year)
    
    df1 = df.sort_values(by='earnings_yield', ascending=False)
    df1['rank_num1'] = np.arange(len(df1))
    df1.set_index('ticker', inplace=True)

    df2 = df.sort_values(by='return_on_tangible_assets', ascending=False)
    df2['rank_num2'] = np.arange(len(df2))
    df2.set_index('ticker', inplace=True)
    df2 = df2['rank_num2']

    df3 = pd.concat([df1, df2], axis=1)

    df3['rank_sum'] = df3['rank_num1'] + df3['rank_num2']

    df3.sort_values('rank_sum', inplace=True)
    df3['rank'] = np.arange(len(df3))

    return df3