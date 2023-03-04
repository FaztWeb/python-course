# This is a guess the number game
import random

guessesTaken = 0

print("Hello! What is your name?")
playerName = input()

number = random.randint(1, 20)
print("Well, " + playerName + ' I am thinking of a number between 1 and 20.')

while guessesTaken < 6:
    print("Take a guess.")
    guess = int(input())
    print(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print("Your guess is too low.")
    if guess > number:
        print("Your guess is too high")
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print("God Job. " + playerName + "! you guessed my number in " + guessesTaken + " guesses!")

if guess != number:
    number = str(number)
    print("Nope. The number of was thinking of was " + number)
