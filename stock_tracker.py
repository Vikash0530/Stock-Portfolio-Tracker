import yfinance as yf

portfolio = {}
total_investment = 0

n = int(input("Enter number of stocks: "))

for i in range(n):
    stock = input("Enter stock symbol (Example: AAPL, TSLA): ").upper()
    quantity = int(input("Enter quantity: "))
    
    portfolio[stock] = quantity

print("\nFetching Real Stock Prices...\n")

for stock, quantity in portfolio.items():
    data = yf.Ticker(stock)
    price = data.info['regularMarketPrice']
    
    investment = price * quantity
    total_investment += investment
    
    print(f"{stock} : {quantity} shares × ${price} = ${investment}")

print("\nTotal Portfolio Value: $", round(total_investment,2))