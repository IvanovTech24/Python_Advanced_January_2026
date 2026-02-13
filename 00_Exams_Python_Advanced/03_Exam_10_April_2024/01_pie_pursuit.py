from collections import deque

contestants = deque(int(x) for x in input().split()) #FIFO
pies = [int(x) for x in input().split()] #LIFO

while contestants and pies:
    contestant = contestants[0]
    pie = pies[-1]

    if contestant >= pie:
        contestant -= pie
        pies.pop()
        if contestant == 0:
            contestants.popleft()
        else:
            contestants.popleft()
            contestants.append(contestant)
    elif pie > contestant:
        pie -= contestant
        contestants.popleft()
        pies.pop()
        if pie == 1:
            if pies:
                pies[-1] += pie
            else:
                pies.append(pie)
        elif pie > 1:
            pies.append(pie)

if not pies and contestants:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join(str(x) for x in contestants)}")
if not pies and not contestants:
    print("We have a champion!")
if not contestants and pies:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join(str(x) for x in pies)}")