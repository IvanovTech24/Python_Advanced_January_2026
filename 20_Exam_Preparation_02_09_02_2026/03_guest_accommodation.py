def accommodate(*guest_group, **available_room):
    accommodation = {}
    unaccommodated_guests = 0
    result = []

    sorted_rooms = sorted(available_room.items(), key=lambda x: (x[1], x[0]))

    for guest in guest_group:
        is_accommodated = False
        for room_key, capacity in sorted_rooms:
            if capacity >= guest:
                room_number = room_key.split("_")[1]
                if room_number not in accommodation:
                    accommodation[room_number] = guest
                    sorted_rooms.remove((room_key, capacity))
                    is_accommodated = True
                    break

        if not is_accommodated:
            unaccommodated_guests += guest

    if accommodation:
        result.append(f"A total of {len(accommodation)} accommodations were completed!")
        for room_number in sorted(accommodation.keys()):
            result.append(f"<Room {room_number} accommodates {accommodation[room_number]} guests>")
    elif not accommodation:
        result.append("No accommodations were completed!")

    if unaccommodated_guests:
        result.append(f"Guests with no accommodation: {unaccommodated_guests}")

    if sorted_rooms:
        result.append(f"Empty rooms: {len(sorted_rooms)}")

    return "\n".join(result)


print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print()
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print()
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))
