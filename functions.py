def function():
    print("Dayum, functions are cool")

def bitcoin_to_usd(btc):
    usd = btc * 527
    print(usd)

function()
bitcoin_to_usd(3.85)


def allowed_dating_age(my_age):
    girls_age = my_age/2 + 7
    return girls_age

my_age = 100
print("Minimum allowed age for:",my_age,"is", allowed_dating_age(my_age))


def get_gender(sex = 'Unkown'):
    if sex == 'm':
        sex = "Male"
    elif sex == 'f':
        sex = "Female"
    print(sex)

get_gender('')