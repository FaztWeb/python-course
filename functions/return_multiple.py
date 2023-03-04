# we can pass return multiple values
# but the true is that python create a tuple an return just a single tuple
def double_values(x, y):
    return x * 2, y *2

a, b = double_values(2,3)

print(a)
print(b)
