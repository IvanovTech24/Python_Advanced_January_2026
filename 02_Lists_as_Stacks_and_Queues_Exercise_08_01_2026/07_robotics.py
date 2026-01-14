from datetime import datetime, timedelta
from collections import deque

robots_input = input().split(";")
robots_dictionary = {}

for robot in robots_input:
    current_robot = robot.split("-")
    robot_name, process_time = current_robot[0], int(current_robot[1])
    robots_dictionary[robot_name] = [process_time, 0]

starting_time = datetime.strptime(input(), "%H:%M:%S")

products = deque()

while True:
    current_product = input()
    if current_product == "End":
        break
    products.append(current_product)

while products:
    starting_time += timedelta(seconds=1)
    product = products.popleft()

    free_robots = deque()
    for name, current_list in robots_dictionary.items():
        if current_list[1] != 0:
            robots_dictionary[name][1] -= 1
        if current_list[1] == 0:
            free_robots.append(name)

    if not free_robots:
        products.append(product)
        continue

    first_free_robots = free_robots.popleft()
    robots_dictionary[first_free_robots][1] = robots_dictionary[first_free_robots][0]

    print(f"{first_free_robots} - {product} [{starting_time.strftime('%H:%M:%S')}]")