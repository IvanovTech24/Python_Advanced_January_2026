def create_set_from_range(range_str):
    start, end = range_str.split(",")
    return set(range(int(start), int(end) + 1))

longest_intersection = set()

for _ in range(int(input())):
    first_range, second_range = input().split("-")
    first_set = create_set_from_range(first_range)
    second_set = create_set_from_range(second_range)

    current_intersection = first_set.intersection(second_set)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")