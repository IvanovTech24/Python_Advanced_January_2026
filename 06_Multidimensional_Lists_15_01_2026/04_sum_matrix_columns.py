n_rows, n_cols = [int(x) for x in input().split(", ")]

matrix = []

for i in range(n_rows):
    data = [int(x) for x in input().split()]
    matrix.append(data)

for column in range(n_cols):
    column_sum = 0
    for row in range(n_rows):
        column_sum += matrix[row][column]
    print(column_sum)