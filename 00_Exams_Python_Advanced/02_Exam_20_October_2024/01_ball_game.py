from collections import deque

def score_manipulation(strength_seq: list[int], accuracy_seq: deque[int], curr_goals: int) \
        -> tuple[list[int], deque[int], int]:
    strength = strength_seq[-1]
    accuracy = accuracy_seq[0]
    result = strength + accuracy

    if result == 100:
        strength_seq.pop()
        accuracy_seq.popleft()
        curr_goals += 1
    elif result < 100:
        if strength < accuracy:
            strength_seq.pop()
        elif strength > accuracy:
            accuracy_seq.popleft()
        elif strength == accuracy:
            strength_seq.pop()
            accuracy_seq.popleft()
            summation_result = strength + accuracy
            strength_seq.append(summation_result)
    elif result > 100:
        strength -= 10
        strength_seq.pop()
        accuracy_seq.popleft()
        strength_seq.append(strength)
        accuracy_seq.append(accuracy)
    return strength_seq, accuracy_seq, curr_goals


strength_sequence = [int(x) for x in input().split()]
accuracy_sequence = deque(int(x) for x in input().split())

total_goals = 0

while strength_sequence and accuracy_sequence:
    strength_sequence, accuracy_sequence, total_goals = (
        score_manipulation(strength_sequence, accuracy_sequence, total_goals))


if total_goals == 3:
    print("Paul scored a hat-trick!")
elif total_goals == 0:
    print("Paul failed to score a single goal.")
elif total_goals > 3:
    print("Paul performed remarkably well!")
elif 0 < total_goals < 3:
    print("Paul failed to make a hat-trick.")

if total_goals:
    print(f"Goals scored: {total_goals}")
if strength_sequence:
    print(f"Strength values left: {', '.join(map(str, strength_sequence))}")
if accuracy_sequence:
    print(f"Accuracy values left: {', '.join(map(str, accuracy_sequence))}")