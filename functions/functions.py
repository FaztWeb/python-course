


# To defie multiple params
def my_multiple(param1, param2, *others):
    for val in others:
        print val

my_multiple(1,2)
my_multiple(1,2,3)
my_multiple(1,2,3,4)

# integers are inmutable
def addOneToNum(num):
    num = num + 1
    print('Value inside function: ', num)
    return
num = 5
addOneToNum(num)
print('Value outside function: ', num)
