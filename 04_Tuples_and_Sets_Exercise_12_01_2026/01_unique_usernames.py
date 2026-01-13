# Solution 1
names = set()
for _ in range(int(input())):
    names.add(input())
for name in names:
    print(name)

# Solution 2
names = set()
for _ in range(int(input())):
    names.add(input())
print("\n".join(names))

# Solution 3
names = set()
for _ in range(int(input())):
    names.add(input())
print(*names, sep="\n")