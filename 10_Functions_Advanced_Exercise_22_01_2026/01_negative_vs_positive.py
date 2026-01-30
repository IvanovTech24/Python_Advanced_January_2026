def sum_nums(*args):
    pos_nums = 0
    neg_nums = 0
    for nums in args:
        if nums > 0:
            pos_nums += nums
        else:
            neg_nums += nums
    return pos_nums, neg_nums

numbers = map(int, input().split())
positive_nums, negative_nums = sum_nums(*numbers)
print(negative_nums)
print(positive_nums)

if positive_nums > abs(negative_nums):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")