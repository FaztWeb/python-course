'mensaje entre comillas simples'
"mensaje entre comillas dobles"
''' a
multi line
message '''

# concatenation
"hello " + "world"

# print("hello " + 1)# eror
"hello " * 10

#'he's my friend'
'he\'s my friend'

# to see all string methods
dir("a string")


"hello"[0] # h
"hello"[1] # e
"hello!"[-1] # !
"Hello"[0:3] # Hel
"Hello!"[1:] # ello!
"Hello!"[-3: -1] # lo
"Hello!"[-3:] # lo!

# conversion
str(5) + str(10) # "510"

"hello".capitalize()
"hello".swapcase()
len("mystring")
"hello world".replace('world', 'Coders')

# to obtain help for a replace method
help("".replace)

# to count o in the string
"hello world".count("o")

# start with
"Hello World".startswith('Hello') # true
"Hello World".endswith('World') # true
"Hello world".split()
"Hello world".split("l") # ['He', '', 'o wor', 'd']
"Hello world".find("e")

"HELLO".lower() #hello
"hello".upper() #HELLO
"hELLO".title() # Hello
