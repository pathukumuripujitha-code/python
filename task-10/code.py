print("BUS PASSENGER OCCUPANCY SIMULATION")

capacity = int(input("Enter bus capacity: "))
passengers = int(input("Enter initial passengers: "))
stops = int(input("Enter number of stops: "))

maximum = passengers
violations = 0

for i in range(stops):
    print("\nStop", i + 1)

    boarding = int(input("Enter boarding passengers: "))
    alighting = int(input("Enter alighting passengers: "))

    if boarding < 0 or alighting < 0:
        print("Invalid passenger count!")
        continue

    elif alighting > passengers:
        print("Invalid: More passengers alighting!")
        continue

    passengers = passengers - alighting + boarding

    if passengers > capacity:
        print("Capacity violation!")
        violations += 1
    else:
        print("Normal occupancy.")

    maximum = max(maximum, passengers)

    print("Current passengers:", passengers)

print("\n----- BUS SUMMARY -----")
print("Final passengers:", passengers)
print("Maximum occupancy:", maximum)
print("Capacity violations:", violations)
print("Available seats:", capacity - passengers)
