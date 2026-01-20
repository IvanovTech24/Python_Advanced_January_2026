def explosion(curr_matrix: list[list[int]],
              curr_cells: tuple[tuple[int, int], ...],
              curr_row: int, curr_col: int, curr_bomb_value: int) -> None:
    for cell in curr_cells:
        new_row = curr_row + cell[0]
        new_col = curr_col + cell[1]
        if 0 <= new_row < rows and 0 <= new_col < rows:
            if curr_matrix[new_row][new_col] > 0:
                curr_matrix[new_row][new_col] -= curr_bomb_value


rows = int(input())
matrix = [[int(x) for x in input().split()] for x in range(rows)]
coordinates = input().split()

curr_coordinates = []

for each in coordinates:
    row, col = map(int, each.split(","))
    curr_coordinates.append((row, col))

cells = (
    (-1, -1), # top left diagonal
    (-1, 0), # top
    (-1, +1), # top right diagonal
    (0, -1), # left
    (0, +1), # right
    (+1, -1), # bottom left diagonal
    (+1, 0), # bottom
    (+1, +1) # bottom right diagonal
)

for coordinate in curr_coordinates:
    if matrix[coordinate[0]][coordinate[1]] <= 0: # exploded bomb validation
        continue
    bomb_value = matrix[coordinate[0]][coordinate[1]]
    matrix[coordinate[0]][coordinate[1]] = 0
    explosion(matrix, cells, coordinate[0], coordinate[1], bomb_value)

alive_cells, sum_alive_cells = 0, 0
for nested_list in matrix:
    for el in nested_list:
        if el > 0:
            alive_cells += 1
            sum_alive_cells += el

print(f"Alive cells: {alive_cells}\nSum: {sum_alive_cells}")
[print(*row, sep=" ") for row in matrix]