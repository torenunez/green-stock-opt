import pandas as pd
from datetime import datetime
from yahoo_finance import Share


def get_stock_data(
        stock_tickers=['AAPL', 'GOOG', 'MSFT', 'AMZN'],
        start_date=None,
        end_date=None):

    if not end_date:
        end_date = datetime.now()

    if not start_date:
        start_date = datetime(end_date.year - 2, end_date.month, end_date.day)

    start_date = start_date.strftime("%Y-%m-%d")
    end_date = end_date.strftime("%Y-%m-%d")

    st_list = []
    return_list = []

    for st in stock_tickers:

        try:
            st_dict = Share(st).get_historical(start_date, end_date)
            st_data = pd.DataFrame.from_dict(st_dict)

            for col in st_data.columns:
                if col not in ['Date', 'Symbol']:
                    st_data[col] = pd.to_numeric(st_data[col], errors='coerce')

            st_data.set_index('Date', drop=True, inplace=True)

            st_list.append(st_data)

            st_return = st_data['Adj_Close'].pct_change()
            return_list.append(st_return)

        except ValueError as ve:
            print('ERROR: Your search string is invalid: {}'.format(ve))

        except Exception as x:
            print(st)
            print("ERROR: {}".format(x))

    returns = pd.concat(return_list, axis=1)
    returns.dropna(axis=0, how='any', inplace=True)
    returns.columns = stock_tickers

    avg_rets = returns.mean()
    cov_mat = returns.cov()

    return st_list, returns, cov_mat, avg_rets