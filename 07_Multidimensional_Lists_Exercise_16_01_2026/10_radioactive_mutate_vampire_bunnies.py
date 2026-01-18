rows, cols = [int(x) for x in input().split()]

matrix = []
player_row, player_col = 0, 0
bunnies = set()

# fill the matrix while simultaneously finding the positions of the player and the rabbit
for row in range(rows):
    matrix.append(list(input()))
    for col in range(cols): # traverse the columns
        if matrix[row][col] == "P":
            player_row, player_col = row, col # position of the player
        elif matrix[row][col] == "B":
            bunnies.add((row, col)) # position of the rabbit

commands = list(input())

has_won = False

# create mapper
moves = {
    "U": lambda r, c: (r - 1, c),
    "D": lambda r, c: (r + 1, c),
    "L": lambda r, c: (r, c - 1),
    "R": lambda r, c: (r, c + 1)
}

# function for bunnies movement
def spread_bunnies(mat, bunnies_set):
    new_bunnies = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for b_row, b_col in bunnies_set:
        for d_row, d_col in directions:
            new_row, new_col = b_row + d_row, b_col + d_col
            if 0 <= new_row < len(mat) and 0 <= new_col < len(mat[0]): # matrix boundary validation
                mat[new_row][new_col] = "B"
                new_bunnies.add((new_row, new_col))

    return mat, bunnies_set.union(new_bunnies)

# player movement
for command in commands:
    new_player_row, new_player_col = moves[command](player_row, player_col)
    matrix, bunnies = spread_bunnies(matrix, bunnies)

    if (player_row, player_col) not in bunnies:
        matrix[player_row][player_col] = "."

    if new_player_row < 0 or new_player_row >= rows or new_player_col < 0 or new_player_col >= cols: # player won validation
        has_won = True
        break

    player_row, player_col = new_player_row, new_player_col
    if matrix[player_row][player_col] == "B":
        break

[print(*row, sep="") for row in matrix]

if has_won:
    print(f"won: {player_row} {player_col}")
else:
    print(f"dead: {player_row} {player_col}")