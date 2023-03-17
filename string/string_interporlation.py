# comma separator
italian_greeting = 'Ciao'
print('Should we greet people with', italian_greeting, 'in North Beach?')

# format
owner = 'Lawrence Ferlinghetti'
age = 100
print('The founder of City Lights Bookstore, {}, is now {} years old.'.format(owner, age))

# f-string
print(f'The founder of City Lights Bookstore, {owner}, is now {age} years old.')

# f-string with expression
print(f'The founder of City Lights Bookstore, {owner.upper()}, is now {age + 1} years old.')

