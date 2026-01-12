n = int(input())

names = set()

for _ in range(n):
    name = input()
    names.add(name)

for current_name in names:
    print(current_name)