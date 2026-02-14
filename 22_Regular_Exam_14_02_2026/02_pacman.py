directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

n = int(input())

matrix = []
packman_position = ()
stars = 0
ghost_position = set()
health = 100
freezer_position = ()
on_freeze = False

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == "P":
            packman_position = (row, col)
            matrix[row][col] = "-"
        elif matrix[row][col] == "*":
            stars += 1
        elif matrix[row][col] == "G":
            ghost_position.add((row, col))
        elif matrix[row][col] == "F":
            freezer_position = (row, col)



while True:
    command = input()
    if command == "end":
        if stars > 0:
            print("Pacman failed to collect all the stars.")
        break

    row, col = packman_position
    row_change, col_change = directions[command]
    new_row, new_col = (row_change + row) % n, (col_change + col) % n
    packman_position = new_row, new_col

    if matrix[new_row][new_col] == "*":
        stars -= 1
    elif matrix[new_row][new_col] == "G":
        if on_freeze:
            on_freeze = False
        else:
            health -= 50
    elif matrix[new_row][new_col] == "F":
        on_freeze = True

    matrix[new_row][new_col] = "-"

    if health <= 0:
        print(f"Game over! Pacman last coordinates [{new_row},{new_col}]")
        break

    if stars == 0:
        print("Pacman wins! All the stars are collected.")
        break

packman_row, packman_col = packman_position
matrix[packman_row][packman_col] = "P"

print(f"Health: {health}")
if stars > 0:
    print(f"Uncollected stars: {stars}")

for row in matrix:
    print("".join(row))