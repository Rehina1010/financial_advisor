import pandas as pd


def load_data():
    sp500_companies = pd.read_csv('data/sp500_companies.zip', compression='zip')
    sp500_index = pd.read_csv('data/sp500_index.zip', compression='zip')
    sp500_stocks = pd.read_csv('data/sp500_stocks.zip', compression='zip')
    return sp500_companies, sp500_index, sp500_stocks
