import yfinance as yf   # yfinance library use hoti hai real stock market data fetch karne ke liye

# Portfolio ek dictionary hai jisme:
# key = stock symbol (AAPL, TSLA)
# value = quantity (kitne shares liye)
portfolio = {}

total_investment = 0   # total portfolio value store karega

# User se pooch rahe hain kitne stocks add karne hain
n = int(input("Enter number of stocks: "))

# Loop chalake har stock ka data input lena
for i in range(n):
    # Stock symbol input (uppercase me convert kar rahe hain consistency ke liye)
    stock = input("Enter stock symbol (Example: AAPL, TSLA): ").upper()
    
    # Quantity (kitne shares user ke paas hain)
    quantity = int(input("Enter quantity: "))
    
    # Dictionary me add kar rahe hain
    portfolio[stock] = quantity

print("\nFetching Real Stock Prices...\n")

# Portfolio ke har stock ke liye loop
for stock, quantity in portfolio.items():
    
    # yf.Ticker() → ek object banata hai jo us stock ka data fetch karta hai
    data = yf.Ticker(stock)
    
    # 'info' dictionary me bohot saari details hoti hain
    # 'regularMarketPrice' current stock price deta hai
    price = data.info['regularMarketPrice']
    
    # Total investment calculate (price × quantity)
    investment = price * quantity
    
    # Overall total me add karna
    total_investment += investment
    
    # Har stock ka result print
    print(f"{stock} : {quantity} shares × ${price} = ${investment}")

# Final total portfolio value print
print("\nTotal Portfolio Value: $", round(total_investment, 2))
# round(..., 2) → value ko 2 decimal places tak limit karta hai
