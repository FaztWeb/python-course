# tuples are inmutables

t = (1, True, "Hello")

print(t)
print(type(t))

# the , operator defines a tuple
t2 = 1, 2, 3

print(t2)
print(type(t2))

print(t2[0])
print(t2[0:2])

index = 0
while index < len(t):
    print(t[index])
    index= index +1

mytuple = (1, 2, 3, 4, 5, 6, 7)

for mynumber in mytuple:
    print(mynumber)


