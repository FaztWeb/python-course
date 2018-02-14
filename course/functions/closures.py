def functionA(x):
    def functionB(y):
        return x + y
    return functionB

add = functionA(5)
print(add(3)) # 8
