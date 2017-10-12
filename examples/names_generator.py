# string to obtain all lowercase letters
# random to select a random letter
import random, string

# to select vowels, because string doesn't privedes
vowels = 'aeiouy'
consonants = 'bcdfghjklmnopqrstvwxz';
letters = string.ascii_lowercase;

# User inputs
print("What Letter do you want?")
print("Enter 'v' for vowels, 'c' for consonants, 'l' for any letter:")
choice1 = input("Enter your first choice: ")
choice2 = input("Enter your second choice: ")
choice3 = input("Enter your third choice: ")

print("You entered: " + choice1 + choice2 + choice3)

def generator():
    if choice1 == 'v':
        letter1 = random.choice(vowels)
    elif choice1 == 'c':
        letter1 = random.choice(consonants)
    elif choice1 == 'l':
        letter1 = random.choice(letters)
    else:
        letter1 = choice1


    if choice2 == 'v':
        letter2 = random.choice(vowels)
    elif choice2 == 'c':
        letter2 = random.choice(consonants)
    elif choice2 == 'l':
        letter2 = random.choice(letters)
    else:
        letter2 = choice2


    if choice3 == 'v':
        letter3 = random.choice(vowels)
    elif choice3 == 'c':
        letter3 = random.choice(consonants)
    elif choice3 == 'l':
        letter3 = random.choice(letters)
    else:
        letter3 = choice3

    name = letter1 + letter2 + letter3
    return name

# to generate 10 diferents names
for i in range(20):
    print(generator())
