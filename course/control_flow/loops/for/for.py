elements = ['one', 'two', 'three']

for element in elements:
    print(element)

# for a multiple lists
names = ['james', 'jhon', 'jack']
email_domains = ['gmail', 'hotmail', 'yahoo']

for i, j in zip(names, email_domains):
    print(i, j)

people = ['aaron', 'ryan', 'joe']
for person in people:
    print('current person: ', person)

# iterate by seq index
for i in range(len(people)):
    print('current person: ', person[i])

for i in range(0, 10):
    print(i)
