from collections import deque

potion_names = [
    ("Brew of Immortality", 110),
    ("Essence of Resilience", 100),
    ("Draught of Wisdom", 90),
    ("Potion of Agility", 80),
    ("Elixir of Strength", 70)
]

substances = [int(x) for x in input().split(", ")]
crystals = deque(int(x) for x in input().split(", "))

crafted_potions = []

while substances and crystals:

    if len(crafted_potions) == 5:
        break

    substance = substances.pop()
    crystal = crystals.popleft()
    current_sum_potion = substance + crystal

    is_founded_potion = False
    for name, energy in potion_names:
        if energy == current_sum_potion and name not in crafted_potions:
            crafted_potions.append(name)
            is_founded_potion = True
            break

    if is_founded_potion:
        continue

    possible = [energy for name, energy in potion_names if energy < current_sum_potion and name not in crafted_potions]
    # possible = []
    # for name, energy in potion_names:
    #   if energy < current_sum_potion and name not in crafted_potions:
    #        possible.append(energy)

    if possible:
        best_energy = max(possible)
        for name, energy in potion_names:
            if energy == best_energy:
                crafted_potions.append(name)
                break

        new_crystal_energy = crystal - 20
        if new_crystal_energy > 0:
            crystals.append(new_crystal_energy)
    else:
        new_crystal_energy = crystal - 5
        if new_crystal_energy > 0:
            crystals.append(new_crystal_energy)

if len(crafted_potions) == 5:
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")

if crafted_potions:
    print(f"Crafted potions: {', '.join(crafted_potions)}")

if substances:
    print(f"Substances: {', '.join(str(x) for x in reversed(substances))}")

if crystals:
    print(f"Crystals: {', '.join(str(x) for x in crystals)}")