from collections import deque

def find_miner_and_coal(curr_mat: list[list[str]]):
    curr_miner = ()
    curr_coal = 0

    for curr_row in range(size_field):
        for curr_col in range(size_field):
            if curr_mat[curr_row][curr_col] == "s":
                curr_miner = (curr_row, curr_col)
            elif curr_mat[curr_row][curr_col] == "c":
                curr_coal += 1
    return curr_miner, curr_coal

def is_valid_position(c_row, c_col):
    return 0 <= c_row < size_field and 0 <= c_col < size_field

size_field = int(input())
commands = deque(input().split())
matrix = [input().split() for _ in range(size_field)]

directions = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1)
}

miner, coal = find_miner_and_coal(matrix)
printed_result = False

while commands:
    command = commands.popleft()
    row, col = miner[0] + directions[command][0], miner[1] + directions[command][1]

    if not is_valid_position(row, col):
        continue

    if matrix[row][col] == "e":
        print(f"Game over! ({row}, {col})")
        printed_result = True
        break

    if matrix[row][col] == "c":
        coal -= 1

    old_row, old_col = miner
    matrix[old_row][old_col] = "*"
    matrix[row][col] = "s"
    miner = (row, col)

    if coal == 0:
        print(f"You collected all coal! ({row}, {col})")
        printed_result = True
        break

if not commands and not printed_result:
    print(f"{coal} pieces of coal left. ({miner[0]}, {miner[1]})")