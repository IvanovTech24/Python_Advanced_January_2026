expression = input()

stack = []
for i in range(len(expression)):
    if expression[i] == "(":
        stack.append(i)
    elif expression[i] == ")":
        start_index = stack.pop()
        end_index = i + 1
        print(expression[start_index:end_index])