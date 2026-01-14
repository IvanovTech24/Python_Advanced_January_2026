from collections import deque

robot_str = input().split(";")
robots = []
for robot in robot_str:
    name, time = robot.split("-")
    robots.append({"name": name, "process_time": int(time), "busy_until_time": 0})

hour, minutes, seconds = map(int, input().split(":"))
start_time_in_seconds = hour * 3600 + minutes * 60 + seconds

products = deque()
while True:
    product = input()
    if product == "End":
        break
    products.append(product)

while products:
    current_product = products.popleft()
    start_time_in_seconds += 1
    is_taken = False
    for robot in robots:
        if robot["busy_until_time"] <= start_time_in_seconds:
            robot["busy_until_time"] = start_time_in_seconds + robot["process_time"]
            h = start_time_in_seconds // 3600
            m = (start_time_in_seconds % 3600) // 60
            s = (start_time_in_seconds % 3600) % 60
            h %= 24
            print(f"{robot['name']} - {current_product} [{h:02d}:{m:02d}:{s:02d}]")
            is_taken = True
            break
    if not is_taken:
        products.append(current_product)