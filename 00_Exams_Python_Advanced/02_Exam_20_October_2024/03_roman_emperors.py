def list_roman_emperors(*args, **kwargs):
    successful_emperors = {}
    unsuccessful_emperors = {}
    result = []

    for name, status in args:
        if status:
            if name in kwargs:
                successful_emperors[name] = kwargs[name]
        else:
            if name in kwargs:
                unsuccessful_emperors[name] = kwargs[name]

    sorted_successful_emperors = sorted(successful_emperors.items(), key=lambda x: (-x[1], x[0]))
    sorted_unsuccessful_emperors = sorted(unsuccessful_emperors.items(), key=lambda x: (x[1], x[0]))

    result.append(f"Total number of emperors: {len(sorted_successful_emperors) + len(sorted_unsuccessful_emperors)}")

    if sorted_successful_emperors:
        result.append(f"Successful emperors:")
        for success_emperors in sorted_successful_emperors:
            result.append(f"****{success_emperors[0]}: {success_emperors[1]}")

    if sorted_unsuccessful_emperors:
        result.append("Unsuccessful emperors:")
        for unsunccess_emperors in sorted_unsuccessful_emperors:
            result.append(f"****{unsunccess_emperors[0]}: {unsunccess_emperors[1]}")

    return "\n".join(result)



# print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14,))
# print("--------------------------------------------")
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False), ("Pertinax", False), ("Vespasian", True), Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19,))
# print("--------------------------------------------")
# print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True), Augustus=40, Trajan=19, Claudius=13,))