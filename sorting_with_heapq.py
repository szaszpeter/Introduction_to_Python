import heapq

grades = [32, 43, 654, 34, 132, 66, 99, 532]

print(heapq.nlargest(3, grades))

stocks = [
    {'ticket': 'appl', 'price': 201},
    {'ticket': 'goog', 'price': 123},
    {'ticket': 'f', 'price': 432},
    {'ticket': 'msft', 'price': 223},
    {'ticket': 'tuna', 'price': 3},
]

print(heapq.nsmallest(2, stocks, key = lambda stock: stock['price']))
