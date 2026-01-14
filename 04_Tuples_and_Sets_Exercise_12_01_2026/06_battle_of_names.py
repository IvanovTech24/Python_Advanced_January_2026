odd_set = set()
even_set = set()

for row in range(1, int(input()) + 1):
    current_number = sum(ord(char) for char in input()) // row

    if current_number % 2 == 0:
        even_set.add(current_number)
    else:
        odd_set.add(current_number)

if sum(even_set) == sum(odd_set):
    print(", ".join(str(x) for x in even_set.union(odd_set)))
elif sum(odd_set) > sum(even_set):
    print(", ".join(str(x) for x in odd_set.difference(even_set)))
else:
    print(", ".join(str (x) for x in even_set.symmetric_difference(odd_set)))

# Solution with different print()
odd_set = set()
even_set = set()

for row in range(1, int(input()) + 1):
    current_number = sum(ord(char) for char in input()) // row

    if current_number % 2 == 0:
        even_set.add(current_number)
    else:
        odd_set.add(current_number)

if sum(even_set) == sum(odd_set):
    print(*even_set | odd_set, sep=", ")
elif sum(odd_set) > sum(even_set):
    print(*odd_set - even_set, sep=", ")
else:
    print(*even_set ^ odd_set, sep=", ")