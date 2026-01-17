portfolio = {}

def add_stock(stock_symbol, quantity, price):
    portfolio[stock_symbol] = {
        'quantity': quantity,
        'price': price
    }


def show_portfolio(current_prices):
    total_investment = 0
    total_value = 0

    for stock, data in portfolio.items():
        quantity = data['quantity']
        price = data['price']
        current_price = current_prices.get(stock, price)  

        investment = quantity * price
        value = quantity * current_price
        profit = value - investment

        total_investment += investment
        total_value += value
        print(f"Stock: {stock} \nQuantity: {quantity} \nPrice: ${price} \nInvestment: ${investment} \nValue: ${value} \nProfit/loss: ${profit} \n\n")

    print(f"Total Investment: ${total_investment}")
    print(f"Total Value: ${total_value}")
    print(f"Overall Profit/loss: ${total_value - total_investment}")


add_stock("AAPL", 10, 150)
add_stock("TSLA", 5, 700)
add_stock("MSFT", 20, 500)
add_stock("GOOGL", 156, 2800)


current_prices = {
    "AAPL": 175,
    "TSLA": 680,
    "MSFT": 300,
    "GOOGL": 2700
}

show_portfolio(current_prices)