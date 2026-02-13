directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

n = int(input())

health = 100
traveller = ()
monster = set()
health_position = ()
exite_position = ()
maze = []
for row in range(n):
    maze.append(list(input()))
    for col in range(n):
        if maze[row][col] == "P":
            traveller = (row, col)
            maze[row][col] = "-"
        elif maze[row][col] == "M":
            monster.add((row, col))
        elif maze[row][col] == "H":
            health_position = (row, col)
        elif maze[row][col] == "X":
            exite_position = (row, col)

while True:
    command = input()
    row, col = traveller
    row_change, col_change = directions[command]
    new_row, new_col = row + row_change, col + col_change
    if 0 <= new_row < n and 0 <= new_col < n:
        if (new_row, new_col) in monster:
            health -= 40
            if health < 0:
                health = 0
                maze[new_row][new_col] = "P"
                monster.remove((new_row, new_col))
                break
            else:
                maze[new_row][new_col] = "-"
                monster.remove((new_row, new_col))
        elif (new_row, new_col) == health_position:
            health += 15
            health = min(100, health)
            maze[new_row][new_col] = "-"
        elif (new_row, new_col) == exite_position:
            traveller = (new_row, new_col)
            maze[traveller[0]][traveller[1]] = "P"
            break
        traveller = (new_row, new_col)
    else:
        new_row, new_col = traveller
        continue

if health <= 0:
    print("Player is dead. Maze over!")
else:
    print("Player escaped the maze. Danger passed!")
print(f"Player's health: {health} units")

for row in maze:
    print("".join(row))