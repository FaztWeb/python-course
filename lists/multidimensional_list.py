matrix = [[ 10, 20, 30 ], [ 40, 50, 60 ], [ 70, 80, 90 ], [20], [30, 40]]

print(matrix)
print(matrix[0][0]) # first row, first column
print(matrix[0][1]) # first row, second column
print(matrix[1][0]) # second row, first column
print(matrix[1][1]) # second row, second column

for row in matrix:
    print(row)

print("---"* 30)

for list in matrix:
    for item in list:
        print(item)

print("---"* 30)
# append a new row to the matrix
matrix.append([100, 200, 300])
print(matrix)
