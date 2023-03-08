# global scope
x = 100

def show_info():
    x = 200
    print(x)

print(x)
show_info()

