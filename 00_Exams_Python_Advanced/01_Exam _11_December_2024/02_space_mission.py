def is_valid_position(r, c, size):
    return 0 <= r < size and 0 <= c < size

def has_reached_planet(curr_mat, r, c):
    return curr_mat[r][c] == "P"

def has_reached_resource_station(curr_mat, r, c):
    return curr_mat[r][c] == "R"

def has_reached_meteorite(curr_mat, r, c):
    return curr_mat[r][c] == "M"

def refuel_spaceship(curr_resources):
    curr_resources += 10
    update_resources = min(100, curr_resources)
    return update_resources

def process_meteorite(curr_mat, r, c, curr_resources):
    new_resources = curr_resources - 5
    curr_mat[r][c] = "."
    return new_resources

n = int(input())

ship_r, ship_c = 0, 0
ship_resources = 100

matrix = []
for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "S":
            ship_r, ship_c = row, col
            matrix[row][col] = "."


def move_spaceship(curr_direction, r, c):
    if curr_direction == "up":
        r = (r - 1)
    elif curr_direction == "down":
        r = (r + 1)
    elif curr_direction == "left":
        c = (c - 1)
    elif curr_direction == "right":
        c = (c + 1)
    return r, c

while True:
    direction = input()
    new_r, new_c = move_spaceship(direction, ship_r, ship_c)
    ship_resources -= 5

    # Boundary check for leaving space
    if not is_valid_position(new_r, new_c, n):
        matrix[ship_r][ship_c] = "S"
        print("Mission failed! The spaceship was lost in space.")
        break

    # Update the spaceship position
    ship_r, ship_c = new_r, new_c

    # Check if the planet is reached (even if resources are zero)
    if has_reached_planet(matrix, new_r, new_c):
        if ship_resources >= 0:
            print(f"Mission accomplished! The spaceship reached Planet B with {ship_resources} resources left.")
            break

    # Check if we have landed on station "R" (recharge)
    if has_reached_resource_station(matrix, new_r, new_c):
        ship_resources = refuel_spaceship(ship_resources)
    elif has_reached_meteorite(matrix, new_r, new_c):
        ship_resources = process_meteorite(matrix, new_r, new_c, ship_resources)

    if ship_resources <= 0:
        matrix[new_r][new_c] = "S"
        print("Mission failed! The spaceship was stranded in space.")
        break

for row in matrix:
    print(" ".join(row))