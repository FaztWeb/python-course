# strings

"Hello World" # double quotes
'Hello World' # single quotes
'''
 Hello
 World
''' # triple quotes

type("Hello")
type('Hello')
type("""
Hello
World
""")

# Numbers

30 # Integers
44.3 # Floating
2 + 3j # complex

type(30)
type(44.3)
type(2 + 3j)

# Booleans

True
False

type(True)
type(False)

# List

[1, 2, 3, 4] # numeric List
[1, 2, 3, 'Hello', 'World'] # any datatype can be inside

type([1, 2, 3, 4])
type([1, 2, 3, 'Hello', 'World'])

# Diccionarios

{"name": "Ryan", "lastname": "Ray"}
{"name": "Joe", "lastname": "McMillan"}

type({"name": "Ryan", "lastname": "Ray"})
type({"name": "Joe", "lastname": "McMillan"})

# None
None
type(None) # NoneType

# check datatype
isinstance('10', str) # True
isinstance(10, str) # False
isinstance(10, int) # True
isinstance("10", int) # False
