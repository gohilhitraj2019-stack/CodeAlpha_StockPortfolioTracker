stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 300
}

stock_name = input("Enter Stock Name: ").upper()
quantity = int(input("Enter Quantity: "))

if stock_name in stock_prices:
    total = stock_prices[stock_name] * quantity

    print("\n----- Investment Summary -----")
    print("Stock:", stock_name)
    print("Quantity:", quantity)
    print("Price Per Share:", stock_prices[stock_name])
    print("Total Investment:", total)

    with open("investment.txt", "w") as file:
        file.write(f"Stock: {stock_name}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Total Investment: {total}\n")

    print("\nResult saved in investment.txt")

else:
    print("Stock not found!")