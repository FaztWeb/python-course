"""
while True:
    myInput = input("> ")
    if myInput == 'bye':
        break;
    else:
        print(myInput)
"""

# 
password = ''

while password != 'python3':
    password = input("Enter your password: ")
    if password == 'python3':
        print('You are logged in')
    else:
        print('Sorry. Try Again')
