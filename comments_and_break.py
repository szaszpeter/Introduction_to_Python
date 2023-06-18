magicNumber = 26

# this is a single line comment
# use ''' ... ''' to skip over multiple lines



'''
for n in range(101):
    if n is magicNumber:
        print(n)
'''


'''for n in range(101):
    print("checking for:", n, "...")
    if n is magicNumber:
        print(n, " is the magic number" )
        break
'''

count = 0
for n in range(100000000):
    if n%4 == 0:
        print(n, " is multiple of 4")
        count += 1

print("Found a total of ", count, "numbers")

