n = int(input())
matrix = []
for i in range(n):
    data = [int(x) for x in input().split()]
    matrix.append(data)

diagonal_sum = 0
for row_col_index in range(n):
    diagonal_sum += matrix[row_col_index][row_col_index]

print(diagonal_sum)