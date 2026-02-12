directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


n, m = map(int, input().split(", "))
matrix = []
time_to_defuse = 16
counter_terrorist = ()
terrorists = set()
bomb = ()
on_bomb = False

for row in range(n):
    matrix.append(list(input()))
    for col in range(m):
        if matrix[row][col] == "C":
            counter_terrorist = (row, col)
        elif matrix[row][col] == "T":
            terrorists.add((row, col))
        elif matrix[row][col] == "B":
            bomb = (row, col)

while True:
    command = input()
    if command in directions.keys():
        time_to_defuse -= 1
        row, col = counter_terrorist
        row_change, col_change = directions[command]
        new_row, new_col = row + row_change, col + col_change
        if 0 <= new_row < n and 0 <= new_col < m:
            counter_terrorist = (new_row, new_col)
            if (new_row, new_col) == bomb:
                on_bomb = True
                continue
            elif (new_row, new_col) in terrorists:
                matrix[new_row][new_col] = "*"
                counter_terrorist = None
                break
            on_bomb = False
    elif command == "defuse" and on_bomb:
        time_to_defuse -= 4
        bomb_row, bomb_col = bomb
        if time_to_defuse >= 0:
            matrix[bomb_row][bomb_col] = "D"
            bomb = None
        else:
            matrix[bomb_row][bomb_col] = "X"
            counter_terrorist = None
            bomb = None
        break
    elif command == "defuse" and not on_bomb:
        time_to_defuse -= 2

    if time_to_defuse <= 0:
        bomb = None
        counter_terrorist = None
        break

if not bomb and not counter_terrorist:
    print("Terrorists win!")
    print("Bomb was not defused successfully!")
    print(f"Time needed: {abs(time_to_defuse)} second/s.")
elif not bomb and counter_terrorist:
    print("Counter-terrorist wins!")
    print(f"Bomb has been defused: {time_to_defuse} second/s remaining.")
elif bomb and not counter_terrorist:
    print("Terrorists win!")

for row in matrix:
    print("".join(row))