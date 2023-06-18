groceries = {"cereal",
             "milk",
             "starcrunch",
             "beer",
             "lotion",
             "beer",
             1}


var = 1
if var in groceries:
    print("You already have", var,"hoss!")
else:
    print("Oh yeah, you need", var)



classmates = {
    "Tony":"cool but smells",
    "Emma":"sits behind me",
    "Lucy":"asks too many questions",
    2:"is a number, but it is still accepted in the dictionary"
}

print(classmates)
print(classmates["Emma"])

for k,v in classmates.items():
    print(k,v)