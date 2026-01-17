# Solution with boolean variable
n = int(input())
matrix = []
for _ in range(n):
    data = list(input())
    matrix.append(data)

searched_symbol = input()
position = None
is_found = False

for row in range(n):
    for col in range(n):
        if matrix[row][col] == searched_symbol:
            position = (row, col)
            is_found = True
            break
    if is_found:
        break

if position:
    print(position)
else:
    print(f"{searched_symbol} does not occur in the matrix")

# Solution with exit() method
n = int(input())
matrix = []
for _ in range(n):
    data = list(input())
    matrix.append(data)

searched_symbol = input()
position = None

for row in range(n):
    for col in range(n):
        if matrix[row][col] == searched_symbol:
            position = (row, col)
            print(position)
            exit()

print(f"{searched_symbol} does not occur in the matrix")