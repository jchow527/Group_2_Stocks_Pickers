import pandas as pd
import portfolio_builder_get_year_data as gy

def get_ranking(year):
    
    df = gy.get_year_data(year)



    sort_by_earnings_yield_df = df.sort_values(by='earnings_yield', ascending=False)
    sort_by_return_on_tangible_assets_df = df.sort_values(by='return_on_tangible_assets', ascending=False)

    dictionary = {}
    rank_by_earnings_yield_df = pd.DataFrame()
    rank_by_earnings_yield = 0
    for symbol in sort_by_earnings_yield_df['ticker']:

        rank_by_earnings_yield = rank_by_earnings_yield + 1

        for variable in ["symbol", "rank_by_earnings_yield"]:
            dictionary[variable] = eval(variable)

        rank_by_earnings_yield_df = rank_by_earnings_yield_df.append(dictionary, ignore_index=True)
    rank_by_earnings_yield_df.set_index('symbol', inplace=True)

    dictionary = {}
    rank_by_return_on_tangible_assets_df = pd.DataFrame()
    rank_by_return_on_tangible_assets = 0
    for symbol in sort_by_return_on_tangible_assets_df['ticker']:

        rank_by_return_on_tangible_assets = rank_by_return_on_tangible_assets + 1

        for variable in ["symbol", "rank_by_return_on_tangible_assets"]:
            dictionary[variable] = eval(variable)

        rank_by_return_on_tangible_assets_df = rank_by_return_on_tangible_assets_df.append(dictionary, ignore_index=True)
    rank_by_return_on_tangible_assets_df.set_index('symbol', inplace=True)


    combined_df = pd.concat([rank_by_earnings_yield_df, rank_by_return_on_tangible_assets_df], axis=1)

    combined_df ['final_rank'] = combined_df ['rank_by_earnings_yield'] + combined_df ['rank_by_return_on_tangible_assets']

    combined_df.sort_values('final_rank', inplace=True)

    return combined_df