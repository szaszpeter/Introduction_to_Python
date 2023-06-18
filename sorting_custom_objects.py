from operator import attrgetter

class User:

    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    def __repr__(self):
        return self.name + " " + str(self.user_id)

users = [
    User('Bucly', 1),
    User('Tom', 13),
    User('July', 144),
    User('Rob', 1444),
    User('Ken', 1532),
    User('Barbie', 1343),
]

for user in users:
    print(user)

print("------------------")

for user in sorted(users, key=attrgetter('name')):
    print(user)

print("------------------")

for user in sorted(users, key=attrgetter('user_id')):
    print(user)