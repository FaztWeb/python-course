class Person():
    # variables
    age = 18

    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    # instance methods need "self"
    def swim(self):
        print("I'm swimming")

    # class methods, allows to use a method without an instance
    @classmethod # this is called a decorator
    def greet(cls, otherPerson):
        print("I'm greeting to " + otherPerson)

# instancing the class
# Object variable
person1 = Person('Joe', 'Canadian')
print(person1.age)

# variable class
print(Person.age) #18

# using methods
person1.swim()

# to use class method
Person.greet('Ryan')
