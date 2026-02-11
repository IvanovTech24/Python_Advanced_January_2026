from collections import deque

bee_group = deque(int(x) for x in input().split())  # FIFO
bee_eaters_group = [int(x) for x in input().split()]  # LIFO

while bee_group and bee_eaters_group:
    current_bee = bee_group.popleft()
    current_bee_eaters = bee_eaters_group.pop()

    while current_bee > 0 and current_bee_eaters > 0:
        if current_bee_eaters * 7 <= current_bee:
            current_bee -= current_bee_eaters * 7
            current_bee_eaters = 0
        else:
            current_bee_eaters -= (current_bee // 7)
            current_bee = 0

    if current_bee > 0 and current_bee_eaters == 0:
        bee_group.append(current_bee)
    elif current_bee == 0 and current_bee_eaters > 0:
        bee_eaters_group.append(current_bee_eaters)

print("The final battle is over!")
if not bee_group and not bee_eaters_group:
    print("But no one made it out alive!")
elif bee_group:
    print(f"Bee groups left: {', '.join(str(el) for el in bee_group)}")
elif bee_eaters_group:
    print(f"Bee-eater groups left: {', '.join(map(str, bee_eaters_group))}")