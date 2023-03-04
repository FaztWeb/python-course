def show_sports(*sports):
    print("Sport 1", sports[0])
    print("Sport 2", sports[1])
    print("Sport 3", sports[2])

show_sports("Football", "Basketball", "Baseball")

def show_names(*names):
    for name in names:
        print(name)

show_names("John", "Mary", "Peter", "Paul")

def my_multiple(param1, param2, *others):
    for val in others:
        print(val)

my_multiple(1,2)
my_multiple(1,2,3)
my_multiple(1,2,3,4)
