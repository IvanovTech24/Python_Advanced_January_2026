# Base Block
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")

# Except Statement
a = [1, 2, 3]
while True:
    try:
        x = int(input("Please enter a number: "))
        print(a[x])
        break
    except (IndexError, ValueError):
        print("Oops! That was no valid number. Try again...")

a = [1, 2, 3]
while True:
    try:
        x = int(input("Please enter a number: "))
        print(a[x])
        break
    except IndexError:
        print(f"Please enter a valid number between 0 and {len(a) - 1}")
    except ValueError:
        print("Please enter a valid number")

Finally
a = [1, 2, 3]
while True:
    try:
        x = int(input("Please enter a number: "))
        print(a[x])
        break
    except IndexError:
        print(f"Please enter a valid number between 0 and {len(a) - 1}")
    except ValueError:
        print("Please enter a valid number")
    finally:
        print("print finally")

# as error
a = [1, 2, 3]
while True:
    try:
        x = int(input("Please enter a number: "))
        print(a[x])
        break
    except IndexError as error:
        print(f"Please enter a valid number between 0 and {len(a) - 1}. Original exception was: {error}")
    except ValueError as error:
        print(f"Please enter a valid number. Original exception was: {error}")
    finally:
        print("print finally")

# else:
a = [1, 2, 3]
while True:
    try:
        x = int(input("Please enter a number: "))
        print(a[x])
    except IndexError as error:
        print(f"Please enter a valid number between 0 and {len(a) - 1}. Original exception was: {error}")
    except ValueError as error:
        print(f"Please enter a valid number. Original exception was: {error}")
    else:
        print("Success")
        break
    finally:
        print("print finally")