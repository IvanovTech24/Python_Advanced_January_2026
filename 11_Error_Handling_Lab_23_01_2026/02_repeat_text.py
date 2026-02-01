text = input()

try:
    times = int(input())
    print(text * times)
except ValueError:
    print("Variable times must be an integer")

# Solution with else:
text = input()

try:
    times = int(input())
except ValueError:
    print("Variable times must be an integer")
else:
    print(text * times)