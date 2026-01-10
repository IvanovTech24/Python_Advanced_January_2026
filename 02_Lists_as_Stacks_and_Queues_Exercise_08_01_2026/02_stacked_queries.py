n = int(input())
stack = []

for _ in range(n):
    query = input().split()
    if query[0] == "1":
        stack.append(int(query[1]))
    elif stack:
        if query[0] == "2":
            stack.pop()
        elif query[0] == "3":
            print(max(stack))
        elif query[0] == "4":
            print(min(stack))
print(", ".join(str(x) for x in reversed(stack)))