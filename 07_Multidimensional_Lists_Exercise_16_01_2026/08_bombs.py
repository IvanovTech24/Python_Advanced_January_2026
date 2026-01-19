def explosion(curr_matrix, curr_cells, curr_row, curr_col, curr_bomb ):
    for cell in curr_cells:
        if 0 <= curr_row + cell[0] < rows and 0 <= curr_col + cell[1] < rows:
            if curr_matrix[curr_row + cell[0]][curr_col + cell[1]] > 0:
                curr_matrix[curr_row + cell[0]][curr_col + cell[1]] -= curr_bomb


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
    if matrix[coordinate[0]][coordinate[1]] <= 0: # validation for dead cells
        continue
    bomb = matrix[coordinate[0]][coordinate[1]]
    matrix[coordinate[0]][coordinate[1]] = 0
    explosion(matrix, cells, coordinate[0], coordinate[1], bomb)

alive_cells, sum_alive_cells = 0, 0
for nested_list in matrix:
    for el in nested_list:
        if el > 0:
            alive_cells += 1
            sum_alive_cells += el

print(f"Alive cells: {alive_cells}\nSum: {sum_alive_cells}")
[print(*row, sep=" ") for row in matrix]