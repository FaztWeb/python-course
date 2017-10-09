age = 0
while age < 18:
    age = age + 1
    print "Congrats, You are " + str(age)

while True:
    myInput = raw_input("> ")
    if myInput == 'bye':
        break;
    else:
        print myInput
