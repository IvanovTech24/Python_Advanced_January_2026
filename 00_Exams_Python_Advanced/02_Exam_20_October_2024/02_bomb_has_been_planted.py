def move_counter_terrorist(curr_command, r, c, mat_row, mat_col):
    if  not (0 <= r < mat_row and 0 <= c < mat_col):
        return r, c

    moves = {
        "up": (-1, 0),
        "down": (+1, 0),
        "left": (0, -1),
        "right": (0, +1)
    }

    row_change, col_change = moves.get(curr_command, (0, 0))
    curr_r, curr_c = (r + row_change), (c + col_change)
    return curr_r, curr_c

input_row, input_col = [int(x) for x in  input().split(", ")]

count_terr_row, count_terr_col = 0, 0
matrix = []
for row in range(input_row):
    matrix.append(list(input()))
    for col in range(input_col):
        if matrix[row][col] == "C":
            count_terr_row, count_terr_col = row, col
            matrix[row][col] = "*"

time_to_defuse = 16

command = input()
while True:
    if command != "defuse":
        time_to_defuse -= 1
        new_row, new_col = move_counter_terrorist(command, count_terr_row, count_terr_col, input_row, input_col)

        if matrix[new_row][new_col] == "B":
            if time_to_defuse >= 1:
                command = input()
                if command == "defuse":
                    if time_to_defuse >= 4:
                        print("Counter-terrorist wins!")
                        print(f"Bomb has been defused: {time_to_defuse} second/s remaining.")
                        break
                    else:
                        continue
        elif matrix[new_row][new_col] == "T":
            matrix[new_row][new_col] = "*"
            print("Terrorists win!")
            break
    elif command == "defuse":
        if matrix[count_terr_row][count_terr_col] != "B":
            time_to_defuse -= 2
            continue
        elif matrix[count_terr_row][count_terr_col] == "B":
            if time_to_defuse >= 4:
                time_to_defuse -= 4
                matrix[count_terr_row][count_terr_col] = "D"
                print("Counter-terrorist wins!")
                print(f"Bomb has been defused: {time_to_defuse} second/s remaining.")
                break
            else:
                needed_time = 4 - time_to_defuse
                matrix[count_terr_row][count_terr_col] = "X"
                print("Terrorists win!")
                print("Bomb was not defused successfully!")
                print(f"Time needed: {needed_time} second/s.")
                break




    count_terr_row, count_terr_col = new_row, new_col
    command = input()

matrix[count_terr_row][count_terr_col] = "C"
for row in matrix:
    print("".join(row))