

balance = float(input("Enter initial balance: "))
limit = float(input("Enter withdrawal limit: "))
n = int(input("Enter number of transactions: "))

total_deposit = 0
total_withdraw = 0
success = 0
rejected = 0

for i in range(n):
    print("\nTransaction", i + 1)
    choice = input("Enter Deposit or Withdrawal: ").lower()
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount! Transaction rejected.")
        rejected += 1

    elif choice == "deposit":
        balance += amount
        total_deposit += amount
        success += 1
        print("Deposit successful.")

    elif choice == "withdrawal":
        if amount > limit:
            print("Withdrawal limit exceeded!")
            rejected += 1
        elif amount > balance:
            print("Insufficient balance!")
            rejected += 1
        else:
            balance -= amount
            total_withdraw += amount
            success += 1
            print("Withdrawal successful.")

    else:
        print("Invalid transaction type!")
        rejected += 1

print("\n----- TRANSACTION SUMMARY -----")
print("Total Deposits:", total_deposit)
print("Total Withdrawals:", total_withdraw)
print("Successful Transactions:", success)
print("Rejected Transactions:", rejected)
print("Final Balance:", balance)
