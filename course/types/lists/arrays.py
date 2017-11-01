['Isaac', 'Aaron', 'Joe', 'Gordon']

len(myArray)

for name in myArray:
    print(name)

[1, 2, 3]  + [4, 5, 6]

if 1 in [1, 2, 3]:
    print('it exits')
else:
    print('does not exits')

myArray[1:]

# ordered a list
# a list is inmutable

sorted([7, 2, 1, 4, 8]) #[1, 2, 4, 7, 8]
sorted([7, 2, 1, 4, 8], reverse = True) #[8, 7, 4, 2, 1]

# to ordered permanently
l = [7, 2, 1, 4, 8]
l.sort()
