print("PROGRESSIVE WATER TARIFF ANALYSIS")

n = int(input("Enter number of households: "))

fixed_fee = 100
penalty = 200
limit = 250

households = []
total_collection = 0

for i in range(n):
    print("\nHousehold", i + 1)

    name = input("Enter household name: ")
    consumption = float(input("Enter water consumption: "))

    if consumption < 0:
        print("Invalid consumption!")
        continue

    # Progressive slab calculation
    if consumption <= 100:
        charge = consumption * 2
    elif consumption <= 200:
        charge = 100 * 2 + (consumption - 100) * 3
    else:
        charge = 100 * 2 + 100 * 3 + (consumption - 200) * 5

    bill = charge + fixed_fee

    if consumption > limit:
        bill += penalty
        status = "Excessive Usage"
    else:
        status = "Normal Usage"

    households.append((name, consumption, bill, status))
    total_collection += bill

    print("Water Bill: Rs.", bill)
    print("Status:", status)

print("\n----- WATER BILL SUMMARY -----")

for name, consumption, bill, status in households:
    print(name, consumption, bill, status)

if households:
    highest = max(households, key=lambda x: x[1])

    print("\nHighest Consumption:", highest[0])
    print("Consumption:", highest[1], "litres")

    print("Total Collection: Rs.", total_collection)

    print("\nExcessive Usage Households:")
    for h in households:
        if h[1] > limit:
            print(h[0])
else:
    print("No valid household records.")
