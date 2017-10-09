# Class
    # properties
    # methods
        # constructor
        # parameters
            #sel

# inheritance
    # simple 
    # multiple

class Person:
    nArms = 0
    nLegs = 0
    hair = True
    colorHair = "Black"
    hungry = False

    def __init__(self):
        self.nArms = 2
        self.nLegs = 2

    def sleep():
        pass

    def eat(self):
        self.hungry = True    

class Man(Person):
    name = 'Default'
    sex = 'M'
    def changeName(self, name):
        self.name = name

class Woman(Person):
    name = 'Default'
    sex = 'F'

isaac = Man()
isaac.eat()
print(isaac.hungry)
