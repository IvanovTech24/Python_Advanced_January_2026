def plant_garden(garden_space: float, *args, **kwargs):
    remaining_space = garden_space
    planted_plants = {}
    is_all_planted = True


    allowed_plants = {}
    for plant_type, plant_space in args:
        if plant_type not in allowed_plants:
            allowed_plants.setdefault(plant_type, plant_space)

    sorted_plant = sorted(kwargs.items(), key=lambda x: x[0])
    for curr_type, quantity in sorted_plant:
        if curr_type in allowed_plants.keys():
            space_per_plant = allowed_plants[curr_type]
            max_possible_space = int(remaining_space / space_per_plant)
            max_planted = min(quantity, max_possible_space)

            if max_planted > 0:
                planted_plants[curr_type] = max_planted
                remaining_space -= max_planted * space_per_plant

            if max_planted < quantity:
                is_all_planted = False

            if remaining_space <= 0:
                has_unplanted = False
                for planted_type, curr_quantity in sorted_plant:
                    if planted_type in allowed_plants:
                        planted_quantity = planted_plants.get(planted_type, 0)
                        if curr_quantity > planted_quantity:
                            has_unplanted = True
                            break

                    if has_unplanted:
                        is_all_planted = False
                    break
    result = []

    if is_all_planted:
        result.append(f"All plants were planted! Available garden space: {remaining_space:.1f} sq meters.")
    else:
        result.append("Not enough space to plant all requested plants!")

    result.append("Planted plants:")

    for p_type in sorted(planted_plants.keys()):
        result.append(f"{p_type}: {planted_plants[p_type]}")
    return "\n".join(result)


print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))
print()
print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, sunflower=5))
print()
print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))
print()
print(plant_garden(50.0, ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, daisy=1))