numbers = tuple([float(x) for x in input().split()])

dictionary = {}

for element in numbers:
    if element not in dictionary:
        dictionary[element] = numbers.count(element)

for key, value in dictionary.items():
    print(f"{key:.1f} - {value} times")