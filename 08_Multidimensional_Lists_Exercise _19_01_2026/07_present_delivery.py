presents = int(input())
n = int(input())

matrix = []
santa = []
nice_kids = 0
for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "S":
            santa = [row, col]
        elif matrix[row][col] == "V":
            nice_kids += 1

nice_kids_gifted = 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while presents > 0:
    command = input()
    if command == "Christmas morning":
        break

    r, c = santa[0] + directions[command][0], santa[1] + directions[command][1]
    if 0 <= r < n and 0 <= c < n:
        if matrix[r][c] == "V":
            presents -= 1
            nice_kids_gifted += 1
            matrix[r][c] = "-"
        elif matrix[r][c] == "C":
            for d in directions.values():
                next_r, next_c = r + d[0], c + d[1]
                if matrix[next_r][next_c] in "VX" and presents > 0:
                    if matrix[next_r][next_c] == "V":
                        nice_kids_gifted += 1
                    presents -= 1
                    matrix[next_r][next_c] = "-"
        matrix[santa[0]][santa[1]] = "-"
        santa = [r, c]
        matrix[r][c] = "S"

if presents < 1 and nice_kids_gifted < nice_kids:
    print("Santa ran out of presents!")

for row in matrix:
    print(*row, sep=" ")

if nice_kids - nice_kids_gifted > 0:
        print(f"No presents for {nice_kids - nice_kids_gifted} nice kid/s.")
else:
    print(f"Good job, Santa! {nice_kids_gifted} happy nice kid/s.")