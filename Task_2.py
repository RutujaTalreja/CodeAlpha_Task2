stock_prices = {
    "TCS": 3500,
    "INFY": 1600,
    "RELIANCE": 2600,
    "HDFC": 1500,
    "WIPRO": 450
}

portfolio = {}  

print("Welcome to Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found. Please choose from available list.")
        continue
    try:
        qty = int(input(f"Enter quantity for {stock}: "))
        if qty <= 0:
            print("Quantity must be greater than 0.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + qty
    except ValueError:
        print("Please enter a valid number.")

total_value = 0
print("\nYour Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock} → {qty} shares × ₹{price} = ₹{value}")

print(f"\nTotal Investment Value: ₹{total_value}")
print("Portfolio Tracking Complete!")
