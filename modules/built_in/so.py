# to import the OS module
import os
# you cab use dir(os) to see all methods
print(os.listdir()) # to list files and directories
# to obtaine the path to the module
print(os.__file__)
# the __init__.py is the the main file of a module

# to use commands from the system
clear = lambda: os.system('clear')
clear()
