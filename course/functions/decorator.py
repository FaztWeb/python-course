def firstDecorator(myFunction):
    def functionDecorated(*args, **kkwars):
        print("first decorator")
    return functionDecorated

@firstDecorator
def myFunction():
    print("my first decorator")

myFunction()

