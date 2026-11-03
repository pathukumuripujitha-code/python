print("FUEL CONSUMPTION AND ROUTE COMPARISON")

distance = float(input("Enter journey distance (km): "))
reserve = float(input("Enter reserve percentage: "))
n = int(input("Enter number of vehicles: "))

feasible = []

for i in range(n):
    print("\nVehicle", i + 1)

    name = input("Enter vehicle name: ")
    mileage = float(input("Enter mileage (km/l): "))
    capacity = float(input("Enter tank capacity (litres): "))
    price = float(input("Enter fuel price per litre: "))

    if mileage <= 0 or capacity <= 0 or price <= 0:
        print("Invalid vehicle details!")
        continue

    fuel = distance / mileage
    reserve_fuel = fuel * reserve / 100
    total_fuel = fuel + reserve_fuel

    if total_fuel <= capacity:
        cost = fuel * price
        feasible.append((name, total_fuel, cost))
        print("Vehicle is feasible.")
        print("Total fuel needed:", round(total_fuel, 2))
        print("Journey cost: Rs.", round(cost, 2))
    else:
        print("Vehicle is not feasible.")
        print("Required fuel:", round(total_fuel, 2))

print("\n----- JOURNEY SUMMARY -----")

if len(feasible) > 0:
    best = min(feasible, key=lambda x: x[2])

    print("Lowest-cost vehicle:", best[0])
    print("Total fuel needed:", round(best[1], 2), "litres")
    print("Lowest journey cost: Rs.", round(best[2], 2))
else:
    print("No feasible vehicle is available.")
