from collections import deque

pumps_number = int(input())
pumps = deque()

for _ in range(pumps_number):
    current_fuel, current_distance = input().split()
    pumps.append({"fuel": int(current_fuel), "distance": int(current_distance)})

start_pumps = 0
visited_pumps = 0

while visited_pumps < pumps_number:
    fuel = 0
    for i in range(pumps_number):
        fuel += pumps[i]["fuel"]
        distance = pumps[i]["distance"]
        if fuel < distance:
            pumps.rotate(-1)
            start_pumps += 1
            visited_pumps = 0
            break
        fuel -= distance
        visited_pumps += 1

print(start_pumps)