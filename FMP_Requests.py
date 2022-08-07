try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json
import pandas as pd

base_string = "https://financialmodelingprep.com/api/v3/"
api_string = "?apikey="


def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

def get_profile(ticker, apikey):
    url = (base_string + "profile/" + ticker + api_string + apikey)
    return get_jsonparsed_data(url)

def get_income_statement(ticker, apikey):
    url = (base_string + "income-statement/" + ticker + api_string + apikey)
    return get_jsonparsed_data(url)


def get_balance_sheet_statement(ticker, apikey):
    url = (base_string + "balance-sheet-statement/" + ticker + api_string + apikey)
    return get_jsonparsed_data(url)

def get_cash_flow_statement(ticker, apikey):
    url = (base_string + "cash-flow-statement/" + ticker + api_string + apikey)
    return get_jsonparsed_data(url)

def get_ratios_ttm(ticker, apikey):
    url = (base_string + "ratios-ttm/" + ticker + api_string + apikey)
    return get_jsonparsed_data(url)

def get_enterprise_values(ticker, apikey):
    url = (base_string + "enterprise-values/" + ticker + api_string + apikey)
    return get_jsonparsed_data(url)

def get_key_metrics(ticker, apikey):
    url = (base_string + "key-metrics/" + ticker + api_string + apikey)
    return get_jsonparsed_data(url)

def get_sp500_constituent(apikey):
    url = (base_string + "sp500_constituent/" + api_string + apikey)
    return get_jsonparsed_data(url)

def get_stock_hist_daily_prices(ticker, start_date, end_date, apikey):
    url = (base_string + "historical-price-full/" + ticker + "?from=" + start_date + "&to=" + end_date + "&apikey=" + apikey)
    response = get_jsonparsed_data(url)
    response_df = pd.DataFrame(response['historical'])
    return response_df

def get_current_stock_price(ticker, apikey):
    url = (base_string + "quote-short/" + ticker + api_string + apikey)
    return get_jsonparsed_data(url)