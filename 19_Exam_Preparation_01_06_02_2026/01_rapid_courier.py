from collections import deque

packages = [int(x) for x in input().split()] #LIFO
couriers = deque(int(x) for x in input().split()) #FIFO

total_weight = 0

while packages and couriers:
    package = packages[-1]
    courier = couriers.popleft()

    if courier >= package:
        courier -= package * 2
        if courier > 0:
            couriers.append(courier)
        total_weight += package
        packages.pop()
    else:
        packages[-1] -= courier
        total_weight += courier

print(f"Total weight: {total_weight} kg")
if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif packages and not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: "
          f"{', '.join(str(p) for p in packages)}")
else:
    print(f"Couriers are still on duty: {', '.join(map(str, couriers))} "
          f"but there are no more packages to deliver.")