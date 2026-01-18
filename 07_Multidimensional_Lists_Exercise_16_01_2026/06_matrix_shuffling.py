def is_valid(r1, c1, r2, c2, row, col):
    return 0 <= r1 < row and 0 <= c1 < col and 0 <= r2 < row and 0 <= c2 < col


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

while True:
    line = input()
    if line == "END":
        break
    command = line.split()

    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in command[1:]]
    if is_valid(row1, col1, row2, col2, rows, cols):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")