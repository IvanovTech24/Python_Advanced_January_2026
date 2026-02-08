n = int(input())

energy = 15
energy_restored = False
min_amount_of_nectar = 30
nectar = 0

#Preserving of the bee
bee_r, bee_c = 0, 0
matrix = []
for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == "B":
            bee_r, bee_c = row, col
            matrix[row][col] = "-"

def move_bee(direction, r, c):
    if direction == "up":
        r = (r - 1) % n
    elif direction == "down":
        r = (r + 1) % n
    elif direction == "left":
        c = (c - 1) % n
    elif direction == "right":
        c = (c + 1) % n
    return r, c

while True:
    energy -= 1
    bee_r, bee_c = move_bee(input(), bee_r, bee_c)

    if matrix[bee_r][bee_c].isdigit():
        nectar += int(matrix[bee_r][bee_c])
        matrix[bee_r][bee_c] = "-"

    if matrix[bee_r][bee_c] == "H":
        if nectar >= min_amount_of_nectar:
            print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
        else:
            print("Beesy did not manage to collect enough nectar.")
        break

    if energy <= 0:
        if not energy_restored and nectar >= min_amount_of_nectar:
            energy += nectar - min_amount_of_nectar
            energy_restored = True
            nectar = min_amount_of_nectar
        else:
            print("This is the end! Beesy ran out of energy.")
            break

matrix[bee_r][bee_c] = "B"
for row in matrix:
    print("".join(row))