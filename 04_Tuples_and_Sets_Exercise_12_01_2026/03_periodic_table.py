# Solution 1
elements = set()
for _ in range(int(input())):
    for el in input().split():
        elements.add(el)
print(*elements, sep="\n")

# Solution 2
elements = set()
for el in range(int(input())):
    elements = elements.union(input().split())
print("\n".join(elements))

#Solution 3
print(*{el for _ in range(int(input())) for el in input().split()}, sep="\n")