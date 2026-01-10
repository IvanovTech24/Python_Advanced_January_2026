n = int(input())
my_stack = []

functions = {
    "1": lambda x: my_stack.append(int(x)),
    "2": lambda: my_stack.pop() if my_stack else None,
    "3": lambda: print(max(my_stack)) if my_stack else None,
    "4": lambda: print(min(my_stack)) if my_stack else None
}

for _ in range(n):
    query = input().split()
    functions[query[0]](*query[1:])

print(*reversed(my_stack), sep=", ")