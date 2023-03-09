import random as rd

# random.random()
# random.random() method returns a random floating point number in the range [0.0, 1.0).
print(rd.random())

# Random integer between 0 and 100
print(rd.randint(0, 100))

# Random float between 17 and 30
print(rd.randint(17, 30))

# random.choice()
# random.choice() method returns a random element from the given sequence.

names = ['John', 'Paul', 'George', 'Ringo']
print(rd.choice(names))

# random.choices()
# random.choices() method returns a list of random elements from the given sequence.
print(rd.choices(names, k=2))

# random.shuffle()
# random.shuffle() method shuffles the elements of a given sequence in place.
print(names)
rd.shuffle(names)
print(names)

# random.sample()
# random.sample() method returns a list of random elements from the given sequence.
print(rd.sample(names, k=2))

# random.uniform()
# random.uniform() method returns a random floating point number between the given range.
print(rd.uniform(1, 10))

# random.randrange()
# random.randrange() method returns a random integer between the given range.
print(rd.randrange(1, 10))
print(rd.randrange(1, 10, 2)) # 2 is the step, so it will return odd numbers
