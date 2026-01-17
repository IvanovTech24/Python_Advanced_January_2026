# Solution with for loop
n = int(input())

matrix = []
for _ in range(n):
    data = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    matrix.append(data)

print(matrix)

# Solution with List Comprehension
n = int(input())
matrix = [[int(x) for x in input().split(", ") if int(x) % 2 == 0] for _ in range(n)]
print(matrix)

# Solution with an even shorter List Comprehension
print([[int(x) for x in input().split(", ") if int(x) % 2 == 0] for _ in range(int(input()))])