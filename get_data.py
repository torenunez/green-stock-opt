import pandas as pd
from datetime import datetime
import pandas_datareader.data as web


# def create_test_data(my_seed=42, num_days=100):
#
#     np.random.seed(my_seed)
#
#     data = np.random.normal(loc=0.001, scale=0.05, size=(num_days, 5))
#     dates = pd.date_range('1/1/2000', periods=num_days, freq='D', tz='UTC')
#     assets = ['asset_a', 'asset_b', 'asset_c', 'asset_d', 'asset_e']
#
#     returns = pd.DataFrame(data, columns=assets, index=dates)
#     avg_rets = returns.mean()
#     cov_mat = returns.cov()
#
#     return returns, cov_mat, avg_rets


def get_stock_data(stock_tickers=['AAPL', 'GOOG', 'MSFT', 'AMZN'], start_date=None, end_date=None):

    if not end_date:
        end_date = datetime.now()

    if not start_date:
        start_date = datetime(end_date.year - 1, end_date.month, end_date.day)

    return_list = []

    for st in stock_tickers:

        st_data = web.DataReader(st, 'google', start_date, end_date)
        st_return = st_data['Close'].pct_change()
        return_list.append(st_return)

    returns = pd.concat(return_list, axis=1)
    returns.dropna(axis=0, how='all', inplace=True)
    returns.columns = stock_tickers

    avg_rets = returns.mean()
    cov_mat = returns.cov()

    return returns, cov_mat, avg_rets