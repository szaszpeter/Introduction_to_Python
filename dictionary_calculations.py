stocks = {
    'GOOG': 434,
    'APPL': 325,
    'FB': 33,
    'AMZN': 44,
    'F': 4444,
}

min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price)
