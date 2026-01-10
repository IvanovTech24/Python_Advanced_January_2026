text = list(input())

#Solution 1
for _ in range(len(text)):
    print(text.pop(), end="")

#Solution 2
stack = []
for i in range(len(text)):
    stack.append(text.pop())
print("".join(stack))