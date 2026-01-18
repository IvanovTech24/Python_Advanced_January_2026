# Solution without list comprehension
n = int(input())

matrix = []
primary_diagonal = []
secondary_diagonal = []

for _ in range(n):
    data = [int(x) for x in input().split()]
    matrix.append(data)

for row_col_index in range(n):
    primary_diagonal.append(matrix[row_col_index][row_col_index])
    secondary_diagonal.append(matrix[row_col_index][-1 - row_col_index])

difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(difference)

# Solution with list comprehension
n = int(input())

matrix = [[int(x) for x in input().split()] for x in range(n)]

primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][-1 - i] for i in range(n)]

diagonal_difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))

print(diagonal_difference)