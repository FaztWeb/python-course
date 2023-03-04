# list
print([10, 11.2, "hello", False])

# list of names
names = ['Isaac', 'Aaron', 'Joe', 'Gordon']

len(names)

for name in names:
    print(name)

print([1, 2, 3]  + [4, 5, 6])

# check if item exists
if 1 in [1, 2, 3]:
    print('item exits')
else:
    print('does not exits')

# split
names[1:]

# ordered a list
# a list is inmutable

sorted([7, 2, 1, 4, 8]) #[1, 2, 4, 7, 8]
sorted([7, 2, 1, 4, 8], reverse = True) #[8, 7, 4, 2, 1]

# to ordered permanently
l = [7, 2, 1, 4, 8]
l.sort()
