n = int(input())

students = {}

for i in range(n):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for name, grades in students.items():
    avg = sum(grades) / len(grades)
    print(f"{name} -> {' '.join([f'{x:.2f}' for x in grades])} (avg: {avg:.2f})")