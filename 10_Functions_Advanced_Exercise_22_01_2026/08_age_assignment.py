# Solution with for loop
def age_assignment(*args, **kwargs):
    persons = {}
    for name in args:
        persons[name] = kwargs[name[0]]

    persons = sorted(persons.items())

    result = []
    for name, age in persons:
        result.append(f"{name} is {age} years old.")

    return "\n".join(result)

# Solution with comprehension
def age_assignment(*args, **kwargs):
    persons = {}
    for name in args:
        persons[name] = kwargs[name[0]]

    persons = sorted(persons.items())

    return "\n".join(f"{name} is {age} years old." for name, age in persons)

print(age_assignment("Peter", "George", G=26, P=19))
print()
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
