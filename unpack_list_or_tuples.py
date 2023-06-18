date, name, price = ['December 23, 2015', 'bread gloves', 8.51]
print(name)

def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)

drop_first_last([65, 76, 98, 54, 21, 100, 100 , 100])


