n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    command = input().split()
    if command[0] == "END":
        break

    row, col, value = map(int, command[1:])
    if row < 0 or row >= n or col < 0 or col >= n:
        print("Invalid coordinates")
        continue

    if command[0] == "Add":
        matrix[row][col] += value
    elif command[0] == "Subtract":
        matrix[row][col] -= value

[print(*row) for row in matrix]