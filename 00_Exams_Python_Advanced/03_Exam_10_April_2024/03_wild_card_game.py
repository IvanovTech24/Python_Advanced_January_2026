def draw_cards(*args, **kwargs):
    monster = []
    spell = []
    result = []

    for c_name, c_type in kwargs.items():
        if c_type == "spell" and c_type not in spell:
            spell.append(c_name)
        elif c_type == "monster" and c_type not in monster:
            monster.append(c_name)

    for c_name, c_type in args:
        if c_type == "spell" and c_type not in spell:
            spell.append(c_name)
        elif c_type == "monster" and c_type not in monster:
            monster.append(c_name)

    sorted_monster = sorted(monster, reverse=True)
    sorted_spell = sorted(spell)

    if sorted_monster:
        result.append("Monster cards:")
        for name in sorted_monster:
            result.append(f"  ***{name}")
    if sorted_spell:
        result.append("Spell cards:")
        for name in sorted_spell:
            result.append(f"  $$${name}")

    return "\n".join(result)

print(draw_cards(("cyber dragon", "monster"), freeze="spell",))
print("========================================================")
print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))
print("========================================================")
print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))
