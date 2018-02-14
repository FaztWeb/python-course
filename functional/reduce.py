from functools import reduce

numbers = (1, 2, 3, 4)

def add(x, y):
    return x + y

result = reduce(add, numbers)
print(result)
