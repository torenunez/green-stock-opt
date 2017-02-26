import portfolioopt as pfopt
import get_data as gd


def section(caption):
    print('\n\n' + str(caption))
    print('-' * len(caption))


def print_portfolio_info(returns, avg_rets, weights):
    """
    Print information on expected portfolio performance.
    """
    ret = (weights * avg_rets).sum()
    std = (weights * returns).sum(1).std()
    sharpe = ret / std
    print("Optimal weights:\n{}\n".format(weights))
    print("Expected return:   {}".format(ret))
    print("Expected variance: {}".format(std ** 2))
    print("Expected Sharpe:   {}".format(sharpe))


def main():
    raw_tickers = input('Enter stocks separated by a comma: ')
    investment = int(input("Enter total investment to allocate: "))

    stock_tickers = raw_tickers.split(", ")
    print(stock_tickers)
    listed_prices, returns, cov_mat, avg_rets = gd.get_stock_data(stock_tickers)

    section("Example returns")
    print(returns.head(10))
    print("...")

    section("Average returns")
    print(avg_rets)

    section("Covariance matrix")
    print(cov_mat)

    section("Minimum variance portfolio (long only)")
    weights = pfopt.min_var_portfolio(cov_mat)
    print_portfolio_info(returns, avg_rets, weights)
    allocation = investment * weights
    print(allocation)

    # Define some target return, here the 70% quantile of the average returns
    target_ret = avg_rets.quantile(0.7)

    section("Markowitz portfolio (long only, target return: {:.5f})".format(target_ret))
    weights = pfopt.markowitz_portfolio(cov_mat, avg_rets, target_ret)
    print_portfolio_info(returns, avg_rets, weights)
    allocation = investment * weights
    print(allocation)


if __name__ == '__main__':
    main()
