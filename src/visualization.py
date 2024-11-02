import matplotlib.pyplot as plt


def plot_price_trend(stock_data, symbol):
    company_data = stock_data[stock_data['Symbol'] == symbol]
    plt.figure(figsize=(10, 5))
    plt.plot(company_data['Date'], company_data['Close'], label=symbol)
    plt.title(f'Price Trend for {symbol}')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()
