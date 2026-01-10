from collections import deque
liters = int(input())
people = deque()
line = input()

while line != "Start":
    people.append(line)
    line = input()

while line != "End":
    if line.isdigit():
        person = people.popleft()
        water_needed = int(line)
        if water_needed <= liters:
            liters -= water_needed
            print(f"{person} got water" )
        else:
            print(f"{person} must wait")
    elif line.startswith("refill"):
        liters += int(line.split()[1])
    line = input()
print(f"{liters} liters left")