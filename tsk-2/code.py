

name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))

# Validate billing constraints
if age <= 0 or consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid patient details or charges")

else:
    total = consultation + diagnostic + treatment

    discount = 0

    # Apply conditional concessions
    if total > 10000:
        discount = 10

    if age >= 60:
        discount += 5

    # Maximum discount is 15%
    if discount > 15:
        discount = 15

    discount_amount = total * discount / 100

    final_bill = total - discount_amount

    # Patient classification
    if final_bill < 5000:
        category = "Low Payment"
    elif final_bill <= 15000:
        category = "Medium Payment"
    else:
        category = "High Payment"

    # Display bill details
    print("\n--- HOSPITAL BILL ---")
    print("Patient Name:", name)
    print("Patient Age:", age)
    print("Consultation Charges:", consultation)
    print("Diagnostic Charges:", diagnostic)
    print("Treatment Charges:", treatment)
    print("Total Bill:", total)
    print("Discount Percentage:", discount, "%")
    print("Discount Amount:", discount_amount)
    print("Final Payable Amount:", final_bill)
    print("Patient Classification:", category)
