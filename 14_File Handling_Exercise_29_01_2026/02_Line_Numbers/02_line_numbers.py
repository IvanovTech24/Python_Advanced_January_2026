from string import punctuation


with open("../text.txt") as file, open("../output.txt", "w") as output_file:
    result = []
    for row_index, line in enumerate(file, 1):
        letter_count = 0
        punctuation_count = 0

        for char in line:
            if char.isalpha():
                letter_count += 1
            elif char in punctuation:
                punctuation_count += 1

        result.append(f"Line {row_index}: {line.strip()} ({letter_count})({punctuation_count})")

    output_file.write("\n".join(result))
