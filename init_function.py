class Tuna:

    def __init__(self):
        print("init is called")

    def swim(self):
        print("I am swimming")

fish = Tuna()
fish.swim()


class Enemy:

    def __init__(self, x):
        self.energy = x

    def printEnergy(self):
        print(self.energy)

jason = Enemy(85)
sandy = Enemy(199)

jason.printEnergy()
sandy.printEnergy()