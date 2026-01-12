# # Definitions
# a = [1, 2, 5]
#
# b = (5, 6, 8)
#
# a.append(100)
# print(a)
#
# # b. #tuple is immutable sequence

# # Methods
# numbers = (1, 2, 1, 3, 1)
# print(numbers.count(1))
# # 3

#------------------------dictionary created----------------
# numbers = tuple([float(x) for x in input().split()])
# data = {}
# for element in numbers:
#     if element in data:
#         data[element] = 0
#     data[element] = 3
#
# print(data)

# n = int(input())
# students = {}
# for i in range(n):
#     name, grade = input().split()
#     if name not in students:
#         students[name] = []
#     students[name].append(float(grade))
# for name, grades in students.items():
#     avg = sum(grades) / len(grades)
#     print(f"{name} -> {' '.join([str(x) for x in grades])} (avg: {avg})")

#--------------------SETS--------------------------------------
#-------------------methods-----------------------------------
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b) # union
print(a.union(b))

print(a & b)
print(a.intersection(b))