from collections import deque

rows, cols = map(int, input().split())
txt = deque(input())

matrix = []

for row in range(rows):
    matrix.append([""] * cols)
    for col in range(cols):
        if row % 2 == 0:
            matrix[row][col] = txt[0]
        else:
            matrix[row][-1 - col] = txt[0]
        txt.rotate(-1)

[print(*row, sep="") for row in matrix]
