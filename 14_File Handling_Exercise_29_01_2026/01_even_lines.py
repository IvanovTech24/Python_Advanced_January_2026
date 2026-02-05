with open("text.txt", "r") as file:
    for index, line in enumerate(file):
        if index % 2 == 0:
            for char in "-,.!?":
                line = line.replace(char, "@")
            print(" ".join(reversed(line.split())))