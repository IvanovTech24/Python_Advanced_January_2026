# Solution 1
text = input()
unique_symbol = set()
for char in text:
    unique_symbol.add(char)
for char in sorted(unique_symbol):
    print(f"{char}: {text.count(char)} time/s")

# Solution 2
text = input()
unique_symbol = sorted(set(text))
for char in unique_symbol:
    print(f"{char}: {text.count(char)} time/s")

# Solution 3
text = input()
[print(f"{char}: {text.count(char)} time/s") for char in sorted(set(text))]

# Solution 4
text = input()
unique_symbol = {char: text.count(char) for char in sorted(set(text))}
print(unique_symbol)