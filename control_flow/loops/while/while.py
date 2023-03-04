# example 1
numero = 1;

while numero <= 10:
	print("hola mundo :" + str(numero))
	numero = numero + 1

# example 2
age = 0
while age < 18:
    age = age + 1
    print "Congrats, You are " + str(age)

# example 3
while True:
    myInput = raw_input("> ")
    if myInput == 'bye':
        break;
    else:
        print myInput
