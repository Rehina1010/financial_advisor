from src.data_processing import load_data
from src.visualization import plot_price_trend
from src.recommendations import investment_recommendation


def main():
    sp500_companies, sp500_index, sp500_stocks = load_data()

    plot_price_trend(sp500_stocks, 'AAPL')

    recommendations = investment_recommendation(sp500_companies)
    for rec in recommendations:
        print(rec)


if __name__ == '__main__':
    main()
