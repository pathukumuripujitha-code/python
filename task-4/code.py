

n = int(input("Enter number of passengers: "))

classes = {
    "Sleeper": 2,
    "AC3": 3,
    "AC2": 4
}

for i in range(n):

    print("\nEnter passenger details")

    name = input("Enter passenger name: ")
    age = int(input("Enter passenger age: "))
    distance = float(input("Enter distance in km: "))

    print("1. Sleeper")
    print("2. AC3")
    print("3. AC2")

    choice = int(input("Select travel class: "))

    # Validate input
    if age < 0 or distance <= 0 or choice not in [1, 2, 3]:
        print("Invalid passenger details")
        continue

    # Select class
    if choice == 1:
        travel_class = "Sleeper"
        rate = 2
    elif choice == 2:
        travel_class = "AC3"
        rate = 3
    else:
        travel_class = "AC2"
        rate = 4

    # Calculate distance slab fare
    if distance <= 100:
        basic = distance * rate
    elif distance <= 200:
        basic = (100 * rate) + (distance - 100) * rate * 0.9
    else:
        basic = (100 * rate) + (100 * rate * 0.9)
        basic += (distance - 200) * rate * 0.8

    # Age concession
    if age < 5:
        concession = basic
    elif age >= 60:
        concession = basic * 0.20
    else:
        concession = 0

    fare = basic - concession
    reservation = 50

    total = fare + reservation

    cancel = input("Cancel ticket? (yes/no): ").lower()

    if cancel == "yes":
        penalty = fare * 0.25
        refund = total - penalty
        status = "Cancelled"
    else:
        penalty = 0
        refund = 0
        status = "Confirmed"

    # Display ticket
    print("\n----- RAILWAY TICKET -----")
    print("Passenger Name:", name)
    print("Age:", age)
    print("Distance:", distance, "km")
    print("Travel Class:", travel_class)
    print("Basic Fare: Rs.", round(basic, 2))
    print("Concession: Rs.", round(concession, 2))
    print("Reservation Fee: Rs.", reservation)
    print("Total Fare: Rs.", round(total, 2))
    print("Ticket Status:", status)
    print("Cancellation Penalty: Rs.", round(penalty, 2))

    if status == "Cancelled":
        print("Refund Amount: Rs.", round(refund, 2))
    else:
        print("Final Payable Amount: Rs.", round(total, 2))

    print("--------------------------")
