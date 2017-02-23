import numpy as np
import pandas as pd
from datetime import datetime
import pandas_datareader.data as web


def create_test_data(my_seed=42, num_days=100):

    np.random.seed(my_seed)

    data = np.random.normal(loc=0.001, scale=0.05, size=(num_days, 5))
    dates = pd.date_range('1/1/2000', periods=num_days, freq='D', tz='UTC')
    assets = ['asset_a', 'asset_b', 'asset_c', 'asset_d', 'asset_e']

    returns = pd.DataFrame(data, columns=assets, index=dates)
    avg_rets = returns.mean()
    cov_mat = returns.cov()

    return returns, cov_mat, avg_rets

##original
my_seed = 42
num_days = 100
np.random.seed(my_seed)
data = np.random.normal(loc=0.001, scale=0.05, size=(num_days, 5))
dates = pd.date_range('1/1/2000', periods=num_days, freq='D', tz='UTC')
assets = ['asset_a', 'asset_b', 'asset_c', 'asset_d', 'asset_e']
returns = pd.DataFrame(data, columns=assets, index=dates)

##pull
end = datetime.now()
start = datetime(end.year - 1,end.month,end.day)
stock_data = web.DataReader("AAPL", 'google', start, end)

