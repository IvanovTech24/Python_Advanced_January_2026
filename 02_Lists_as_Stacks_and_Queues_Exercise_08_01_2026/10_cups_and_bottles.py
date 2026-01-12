from collections import deque

cups = deque(int(x) for x in input().split())
bottles = list(int(x) for x in input().split())

water_left = 0

while cups and bottles:
    cup = cups.popleft()
    bottle = bottles.pop()

    if cup <= bottle:
        water_left += bottle - cup
    else:
        cups.appendleft(cup)
        cups[0] -= bottle

if cups:
    print(f"Cups: {' '.join(str(x) for x in cups)}")
elif bottles:
    print(f"Bottles: {' '.join(str(x) for x in bottles)}")

print(f"Wasted litters of water: {water_left}")