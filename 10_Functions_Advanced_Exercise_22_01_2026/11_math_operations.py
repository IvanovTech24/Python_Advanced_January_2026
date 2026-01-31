"""
1. Create a mapper with mathematical operations for each of the keys.
2. Store all the keys in a single variable to be able to iterate through them.
3. Using a for loop, iterate through the length of the positional arguments (*args):
    3.1 Store the key index in a variable so that when the last index of the positional arguments is reached,
    the cycle starts over (using modulo % or a reset logic).
    3.2 Store the type of mathematical operation in a variable based on the current key.
    3.3 Overwrite the value in the keyword arguments dictionary (**kwargs) with the new value obtained
    from the anonymous function (lambda).
4. Store the result of the data sorting in a variable.
5. Return the final result from the function.
"""

def math_operations(*args, **kwargs):
    calculates = {
        "a": lambda x, y: x + y,
        "s": lambda x, y: x - y,
        "d": lambda x, y: x / y if y != 0 else x,
        "m": lambda x, y: x * y
    }

    keys = list(calculates.keys())
    for i in range(len(args)):
        key = keys[i % 4]
        calculate = calculates[key]
        kwargs[key] = calculate(kwargs[key], args[i])

    result = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    return "\n".join([f"{k}: {v:.1f}" for k, v in result])


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))

print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))

print(math_operations(6.0, a=0, s=0, d=5, m=0))