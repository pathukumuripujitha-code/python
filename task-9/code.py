print("TEXT-BASED INVOICE DATA EXTRACTION")

n = int(input("Enter number of invoice records: "))

total = 0
valid = 0
invalid = 0

for i in range(n):
    print("\nInvoice", i + 1)

    record = input("Enter invoice (Code,Quantity,Amount): ")
    parts = record.split(",")

    if len(parts) == 3:
        code = parts[0].strip()
        qty = parts[1].strip()
        amount = parts[2].strip()

        try:
            quantity = int(qty)
            price = float(amount)

            if code != "" and quantity > 0 and price > 0:
                print("Product Code:", code)
                print("Quantity:", quantity)
                print("Amount: Rs.", price)

                total += price
                valid += 1
            else:
                print("Malformed invoice record!")
                invalid += 1

        except ValueError:
            print("Invalid quantity or amount!")
            invalid += 1

    else:
        print("Malformed invoice record!")
        invalid += 1

print("\n----- INVOICE SUMMARY -----")
print("Valid Records:", valid)
print("Invalid Records:", invalid)
print("Total Invoice Amount: Rs.", round(total, 2))
