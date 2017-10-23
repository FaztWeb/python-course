# consider identation
def nothing():
    pass

# the string is called, "docstring"

def my_function(param1, param2):
    """This functions print params"""
    print param1
    print param2

my_function('Hello', "World")

# to indicate the params
my_function(param2 = "World", param1="Hello")

# To Assign default values
def myPrinter(text, times = 1):
    print text * times

myPrinter("Hi")
myPrinter("Hi", 6)

# To defie multiple params
def my_multiple(param1, param2, *others):
    for val in others:
        print val

my_multiple(1,2)
my_multiple(1,2,3)
my_multiple(1,2,3,4)

# to return a value
def sum(x, y):
    return x + y

print sum(2,3)

# we can pass return multiple values
# but the true is that python create a tuple an return just a single tuple
def f(x, y):
    return x * 2, y *2
a, b = f(2,3)

print a
print b

# integers are inmutable
def addOneToNum(num):
    num = num + 1
    print('Value inside function: ', num)
    return
num = 5
addOneToNum(num)
print('Value outside function: ', num)
