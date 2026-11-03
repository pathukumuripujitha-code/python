

name = input("Enter customer name: ")

data_used = float(input("Enter monthly data usage (GB): "))
calls_used = float(input("Enter monthly call usage (minutes): "))
required_days = int(input("Enter required validity days: "))
budget = float(input("Enter your budget: "))

n = int(input("Enter number of mobile plans: "))

plans = []
eligible = []

for i in range(n):
    print("\nEnter Plan", i + 1, "Details")

    plan_name = input("Enter plan name: ")
    price = float(input("Enter plan price: "))
    data_limit = float(input("Enter data limit (GB): "))
    call_limit = float(input("Enter call limit (minutes): "))
    validity = int(input("Enter validity days: "))

    data_rate = float(input("Excess data charge per GB: "))
    call_rate = float(input("Excess call charge per minute: "))

    # Calculate excess usage
    extra_data = max(0, data_used - data_limit)
    extra_calls = max(0, calls_used - call_limit)

    data_charge = extra_data * data_rate
    call_charge = extra_calls * call_rate

    total_cost = price + data_charge + call_charge

    plan = {
        "name": plan_name,
        "cost": total_cost,
        "data_charge": data_charge,
        "call_charge": call_charge,
        "validity": validity
    }

    plans.append(plan)

    # Check eligibility
    if (data_limit >= data_used and
        call_limit >= calls_used and
        validity >= required_days and
        total_cost <= budget):

        eligible.append(plan)

# Display plan details
print("\n----- PLAN COMPARISON -----")

for plan in plans:
    print("\nPlan:", plan["name"])
    print("Total Cost:", round(plan["cost"], 2))

# Select economical eligible plan
print("\n----- BEST MOBILE PLAN -----")

if len(eligible) > 0:

    best = min(eligible, key=lambda x: x["cost"])

    print("Customer Name:", name)
    print("Best Plan:", best["name"])
    print("Total Cost: Rs.", round(best["cost"], 2))
    print("Data Excess Charge: Rs.",
          round(best["data_charge"], 2))
    print("Call Excess Charge: Rs.",
          round(best["call_charge"], 2))
    print("Validity:", best["validity"], "days")
    print("Remaining Budget: Rs.",
          round(budget - best["cost"], 2))

else:
    print("No eligible mobile plan found.")
