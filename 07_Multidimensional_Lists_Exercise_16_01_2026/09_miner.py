from collections import deque

def find_miner_and_coal(curr_matrix: list[list[str]]) -> tuple[tuple[int, int], int]:
    curr_miner = ()
    curr_coal = 0

    for curr_row in range(size_field):
        for curr_col in range(size_field):
            if curr_matrix[curr_row][curr_col] == "s":
                curr_miner = (curr_row, curr_col)
            elif curr_matrix[curr_row][curr_col] == "c":
                curr_coal += 1
    return curr_miner, curr_coal

def is_valid_position(c_row: int, c_col: int) -> bool:
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

miner_position, total_coal = find_miner_and_coal(matrix)
game_result = False

while commands:
    command = commands.popleft()
    row, col = miner_position[0] + directions[command][0], miner_position[1] + directions[command][1]

    if not is_valid_position(row, col):
        continue

    if matrix[row][col] == "e":
        print(f"Game over! ({row}, {col})")
        game_result = True
        break

    if matrix[row][col] == "c":
        total_coal -= 1

    old_row, old_col = miner_position
    matrix[old_row][old_col] = "*"
    matrix[row][col] = "s"
    miner_position = (row, col)

    if total_coal == 0:
        print(f"You collected all coal! ({row}, {col})")
        game_result = True
        break

if not commands and not game_result:
    print(f"{total_coal} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")