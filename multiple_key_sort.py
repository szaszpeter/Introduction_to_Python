from operator import itemgetter

stocks = [
    {'ticket': 'appl', 'price': 123},
    {'ticket': 'goog', 'price': 123},
    {'ticket': 'f', 'price': 432},
    {'ticket': 'msft', 'price': 432},
    {'ticket': 'tuna', 'price': 3},
]

# Single Key sort
for x in sorted(stocks, key = itemgetter('price')):
    print(x)

print("-----------------------")

# Multiple Key sort
for x in sorted(stocks, key=itemgetter('price', 'ticket')):
    print(x)