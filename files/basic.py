# to otpen a file
fo = open('text.txt', 'w')

# Get some info
print('Name: ', fo.name) # text.txt
print('Is Closed: ', fo.closed) # False
print('Opening mode:', fo.mode) #w

# write in the file
fo.write('practice with python')
fo.write(' and files')
fo.write('\nand another line')
fo.close() # to save text in files and close

# w for rewrite, a to append
fo = open('text.txt', 'a')
fo.write('writing something')
fo.close()

# to add with multiple lines
fo = open('text.txt', 'w')
l = ['line1', 'line2', 'line3']
for item in l:
    fo.write(item + '\n')
fo.close()

# read from file
fo = open('text.txt', 'r+')
text = fo.read(10) #read just 10 characters
print(text)
fo.close()

# to create a new file
fo = open('text2.txt', 'w+')
fo.write('this is a new file')
fo.close()

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
