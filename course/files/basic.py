# To read files
file = open('data.txt', 'r')

type(file) # textIOWrapper

content = file.read() 

type(content) #str

# this returns [] because the pointer
# is not in the beginning
content = file.readlines()

# so we have to use 
file.seek(0)

# and then we can obtain a list of the content
content = file.readlines()

# to remove \n we can use rstrip to compare
content = [i.rstrip("\n") for i in content]

# To Open Files
