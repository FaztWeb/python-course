# lists
# tuples
# dictionaries

l = [22, True, "Hello", [1,2]]

print l[0] # 22
print l[3][0] #1

# To Mofify a value
l[3][1] = 3
print l

# Slicing or particioning a List
l = ['One', 'Two', 'Three', 'Four', 'Five', 'Six']
print l[0:2] # One, Two
print l[0:6:2] # One, Three, Five

print l[1:] # Two, Three, Four, Five, Six
print l[:2] # One, Two
print l[:] #'One', 'Two', 'Three', 'Four', 'Five', 'Six'
print l[::2] # One, Three, Five

l[0:2] = [1,2]
print l #[1, 2, 'Three', 'Four', 'Five', 'Six']
