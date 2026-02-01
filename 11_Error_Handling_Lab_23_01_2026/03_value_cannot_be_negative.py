class ValueCannotBeNegative(Exception):
    pass

n = int(input())

for _ in range(5):
    num = int(input())
    if num < 0:
        raise ValueCannotBeNegative