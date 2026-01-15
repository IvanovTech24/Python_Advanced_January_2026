from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

points = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

toys = {}

while materials and magic:
    total_magic = materials[-1] * magic[0]
    if total_magic in points.keys():
        materials.pop()
        magic.popleft()
        new_toy = points[total_magic]
        if new_toy not in toys:
            toys[new_toy] = 0
        toys[new_toy] += 1
    elif total_magic < 0:
        materials.append(materials.pop() + magic.popleft())
    elif total_magic > 0:
        magic.popleft()
        materials[-1] += 15
    else:
        if materials[-1] == 0:
            materials.pop()
        if magic[0] == 0:
            magic.popleft()

if ("Doll" in toys and "Wooden train" in toys) or ("Teddy bear" in toys and "Bicycle" in toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for key, value in sorted(toys.items()):
    print(f"{key}: {value}")