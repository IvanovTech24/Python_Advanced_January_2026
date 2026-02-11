def move_player(direction: str, r: int, c: int, curr_n: int) -> tuple[int, int]:
    moves = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }
    row_change, col_change = moves.get(direction, (0, 0))
    new_row, new_col = (r + row_change), (c + col_change)

    if (new_row < 0 or new_row >= curr_n)  or (new_col < 0 or new_col >= curr_n):
        return 0, 0

    return new_row, new_col


n = int(input())

collected_stars = 2
player_row, player_col = 0, 0

matrix = []
for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "P":
            player_row, player_col = row, col
            matrix[row][col] = "."

while True:
    command = input()
    new_player_row, new_player_col = move_player(command, player_row, player_col, n)


    if matrix[new_player_row][new_player_col] == "*":
        collected_stars += 1
        matrix[new_player_row][new_player_col] = "."
    elif matrix[new_player_row][new_player_col] == "#":
        collected_stars -= 1
        if collected_stars <= 0:
            print("Game over! You are out of any stars.")
            break
        continue

    player_row, player_col = new_player_row, new_player_col

    if collected_stars == 10:
        print(f"You won! You have collected {collected_stars} stars.")
        break

matrix[player_row][player_col] = "P"

print(f"Your final position is [{player_row}, {player_col}]")
for row in matrix:
    print(" ".join(row))