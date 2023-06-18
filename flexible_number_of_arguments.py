def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    return total

print(add_numbers(1,2,3,4,5))
print(add_numbers(1,2,3,4))
print(add_numbers(1,2,3))
print(add_numbers(1,2))