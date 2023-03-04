

# integers are inmutable
def addOneToNum(num):
    num = num + 1
    print('Value inside function: ', num)
    return
num = 5
addOneToNum(num)
print('Value outside function: ', num)
