class Girl:

    gender = "female"

    def __init__(self,name):
        self.name = name


r = Girl('Rachel')
s = Girl('Rachel')

print(r.gender + " " + r.name)
print(str(r))
print(str(s))