# Solution with list comprehension
n = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]

primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][-1 - i] for i in range(n)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")

# Solution without list comprehension
n = int(input())

matrix = []
primary_diagonal = []
secondary_diagonal = []

for _ in range(n):
    data = [int(x) for x in input().split(", ")]
    matrix.append(data)

for row_col_index in range(n):
    primary_diagonal.append(matrix[row_col_index][row_col_index])
    secondary_diagonal.append(matrix[row_col_index][-1 - row_col_index])

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")