clothes = list(map(int, input().split()))
rack_capacity = int(input())

racks = 0

while clothes:
    racks += 1
    current_rack = rack_capacity
    while clothes and clothes[-1] <= current_rack:
        current_rack -= clothes.pop()

print(racks)