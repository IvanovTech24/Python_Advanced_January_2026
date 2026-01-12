n = int(input())

reservations = set()

for _ in range(n):
    reservation = input()
    reservations.add(reservation)

reservation = input()

while reservation != "END":
    reservations.remove(reservation)
    reservation = input()

print(len(reservations))
sorted_reservations = sorted(reservations)

for current_reservation in sorted_reservations:
    print(current_reservation)