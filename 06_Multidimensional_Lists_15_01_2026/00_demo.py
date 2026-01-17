#-----------------------------------matrix view-----------------------------------
multidimensional_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#-------------------------------------find 9-----------------------------------
print(multidimensional_list[2][2])

#----------------------------------assign value----------------------------------
print(multidimensional_list)
multidimensional_list[1][2] = 100
print(multidimensional_list)

#---------------------------------Create matrix---------------------------------------
matrix = []
for i in range(3):
    matrix.append([])
    for _ in range(2):
        matrix[i].append(0)
print(matrix)

matrix = []
for i in range(3):
    matrix.append([])
    for j in range(1, 4):
        matrix[i].append(j)
print(matrix)

#--------------------------Multidimensional List Comprehension----------------------
matrix = [[0 for j in range(2)] for i in range(3)]
print(matrix)

matrix = []
for i in range(3):
    matrix.append([0 for j in range(2)])
print(matrix)

matrix = [[j for j in range(1, 4)] for i in range(3)]
print(matrix)

#------------------------Flattening a matrix----------------------------------------
matrix = [[1, 2, 3], [4, 5, 6]]
flattened_matrix = [el for row in matrix for el in row]
print(flattened_matrix)

# implemented using a for loop
matrix = [[1, 2, 3], [4, 5, 6]]
flattened_matrix = []
for row in matrix:
    for el in row:
        flattened_matrix.append(el)
print(flattened_matrix)

# 3D dimensional
matrix = [
    [
        [1, 2], [3, 4],
        [5, 6], [7, 8]
    ]
]

print(matrix[0][1][1])

#---------------------Traversing a column in matrix-----------------------
n_rows = 3
n_cols = 6
matrix = [
    [7, 1, 3, 3, 2, 1],
    [1, 3, 9, 8, 5, 6],
    [4, 6, 7, 9, 1, 0]
]
for column in range(n_cols):
    column_sum = 0
    for row in range(n_rows):
        column_sum += matrix[row][column]
    print(column_sum)
