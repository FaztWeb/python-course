double = lambda x: x * 2
print(double(5))

# display a string with a lambda function
sayHello = lambda x: "Hello " + x
print(sayHello("World"))

# display a string with a lambda function
(lambda x: "Hello " + x)("World")

# multiple arguments
calculate = lambda x, y, z: x * y + z
print(calculate(2, 3, 4))

# if else with lambda function
calculate = lambda x, y : x if x > y else y
print(calculate(2, 3))

calculate = lambda x, y : x if (x > y) else y
print(calculate(5, 3))

