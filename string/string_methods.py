# capitalize
message = "hello world"
print(message.capitalize())

# casefold
message = "HELLO WORLD"
print(message.casefold())

# center
message = "hello"
print(message.center(20, "*"))
print(message.center(20, "_"))
print(message.center(20, "#"))

# count 
message = "hello world"
print(message.count("l"))
print(message.count("o"))
print(message.count("o", 0, 5)) # count from 0 to 5

message = "awesome language, awesome community"
print(message.count("awesome"))

# find
message = "hello web, hello python"
print(message.find("o"))
print(message.find("o", 5, 10)) # find from 0 to 5, return -1
print(message.find("python"))

# endswith
message = "hello world"
print(message.endswith("d"))
print(message.endswith("world"))
print(message.endswith("world", 0, 5)) # endswith from 0 to 5
print(message.endswith("p"))

# expandtabs
message = "hello\tworld"
print(message)
print(message.expandtabs(20))
print(message.expandtabs(10))

# index
message = "hello world"
print(message.index("o"))
print(message.index("o", 5, 10)) # return 4

# isalnum
message = "hello"
print(message.isalnum())
message = "hello123"
print(message.isalnum())

# isalpha
message = "hello"
print(message.isalpha())
message = "hello123"
print(message.isalpha())

# isdecimal
message = "123"
print(message.isdecimal())
message = "123.45"
print(message.isdecimal()) # not decimal, because it has a dot

# isdigit
message = "123"
print(message.isdigit())
message = "123.45"
print(message.isdigit()) # not digit, because it has a dot

# isidentifier
message = "hello"
print(message.isidentifier())
message = "hello world"
print(message.isidentifier())
message = "hello_world"
print(message.isidentifier())
message = "hello123"
print(message.isidentifier())
message = "123hello"
print(message.isidentifier())

# islower
message = "hello"
print(message.islower())
message = "HELLO"
print(message.islower())

# isnumeric
message = "123"
print(message.isnumeric())
message = "123.45"
print(message.isnumeric()) # not numeric, because it has a dot

# isprintable
message = "hello"
print(message.isprintable())
message = "hello world"
print(message.isprintable())
message = "hello\tworld"
print(message.isprintable())

# isspace
message = " "
print(message.isspace())
message = "hello"
print(message.isspace())

# istitle
message = "Hello"
print(message.istitle()) # True
message = "hello"
print(message.istitle()) # False

# isupper
message = "HELLO"
print(message.isupper()) # True
message = "hello"
print(message.isupper()) # False
message = "HeLLO WORLD"
print(message.isupper()) # False

# join
message = "python"
print(message.join("123")) # 1python2python3
print(message.join(["1", "2", "3"])) # 1python2python3
message = {"python", "java", "c"}
separator = "__"
print(separator.join(message)) # java__c__python

# ljust
message = "hello"
print(message.ljust(20, "*"))
print(message.ljust(20, "_"))
print(message.ljust(20, "#"))

# lower
message = "HELLO"
print(message.lower())
message = "Hello"
print(message.lower())

# lstrip
message = " hello "
print(message.lstrip())
message = "######hello"
print(message.lstrip("#"))

# partition
message = "hello world"
print(message.partition(" "))
print(message.partition("o"))
print(message.partition("z"))

# removeprefix
message = "hello world"
print(message.removeprefix("hello"))

# removesuffix
message = "hello world"
print(message.removesuffix("world"))

# replace
message = "hello world"
print(message.replace("o", "a"))
print(message.replace("o", "a", 1)) # replace only one occurrence
message = "hello world, hello python, hello fazt"
print(message.replace("hello", "hi"))
print(message.replace("hello", "hi", 2)) 

# rfind
message = "hello world"
print(message.rfind("o"))
print(message.rfind("o", 0, 5)) 
print(message.rfind("python"))
message = "hello world, hello python, hello fazt"
print(message.rfind("hello"))

# rindex
message = "hello world"
print(message.rindex("o"))
print(message.rindex("o", 0, 5))
# print(message.rindex("python")) # ValueError: substring not found
message = "hello world, hello python, hello fazt"
print(message.rindex("hello"))

# rjust
message = "hello"
print(message.rjust(20, "*"))
print(message.rjust(20, "_"))
print(message.rjust(20, "#"))

# rpartition
message = "hello world"
print(message.rpartition(" "))
print(message.rpartition("o"))
print(message.rpartition("z"))

# rsplit
message = "hello world"
print(message.rsplit())
message = "hello world, hello python, hello fazt"
print(message.rsplit(","))
print(message.rsplit(",", 1))

# rstrip
message = " hello "
print(message.rstrip())
message = "hello######"
print(message.rstrip("#"))

# split
message = "hello world"
print(message.split())
message = "hello world, hello python, hello fazt"
print(message.split(","))
print(message.split(",", 1))

# splitlines
message = "hello\nworld\npython\nfazt"
print(message.splitlines())
print(message.splitlines(True))
print(message.splitlines(False))

# startswith
message = "hello world"
print(message.startswith("h"))
print(message.startswith("hello"))
print(message.startswith("hello", 0, 5))
print(message.startswith("p"))

# strip
message = " hello "
print(message.strip())
message = "######hello######"
print(message.strip("#"))

# swapcase
message = "hello world"
print(message.swapcase())
message = "HELLO WORLD"
print(message.swapcase())

# title
message = "hello world"
print(message.title())
message = "hello world, hello python, hello fazt"
print(message.title())

# translate
message = "hello world"
print(message.translate({ord("h"): "H"}))
print(message.translate({ord("h"): "H", ord("o"): "O"}))
print(message.translate({ord("h"): "H", ord("o"): "O", ord("l"): "L"}))

# upper
message = "hello world"
print(message.upper())
message = "HELLO WORLD"
print(message.upper())

# zfill
message = "hello"
print(message.zfill(20))




"hello".swapcase()

# start with
"Hello world".split()
"Hello world".split("l") # ['He', '', 'o wor', 'd']

# to obtain help for a replace method
# help("".replace)