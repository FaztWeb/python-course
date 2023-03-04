def my_function(param1, param2):
    print(param1)
    print(param2)

my_function('Hello', "World")

# to indicate the params
my_function(param2 = "World", param1="Hello")

def duplicate_points(username, points):
    print(username, points * 2)

duplicate_points("John", 10.33)
duplicate_points(points=100.44, username="David")
