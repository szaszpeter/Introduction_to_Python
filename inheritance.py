class Parent():

    def print_last_name(self):
        print("Roberts")


class Child(Parent):

    def __init__(self, first_name):
        self.first_name = first_name

    def print_first_name(self):
        print(self.first_name)

    def print_last_name(self):
        print("Snitzelber")

child1 = Child("Bucky")
child1.print_first_name()
child1.print_last_name()