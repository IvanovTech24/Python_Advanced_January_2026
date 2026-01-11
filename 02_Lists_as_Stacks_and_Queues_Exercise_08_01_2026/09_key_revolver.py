from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(int(x) for x in input().split())
money = int(input())

shots = 0

while bullets and locks:
    shots += 1
    current_bullet = bullets.pop()
    money -= bullet_price

    if locks[0] >= current_bullet:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")

    if shots == barrel_size and bullets:
        print("Reloading!")
        shots = 0

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${money}")