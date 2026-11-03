

name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")

basic = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))
hours = float(input("Enter overtime hours: "))
rate = float(input("Enter overtime rate per hour: "))
incentives = float(input("Enter incentives: "))

# Validate input
if (basic < 0 or allowances < 0 or
    hours < 0 or rate < 0 or incentives < 0):

    print("Invalid salary details")

else:
    # Calculate overtime pay
    overtime = hours * rate

    # Calculate gross salary
    gross = basic + allowances + overtime + incentives

    # Progressive deduction
    if gross < 20000:
        percentage = 5
    elif gross <= 40000:
        percentage = 10
    else:
        percentage = 15

    deduction = gross * percentage / 100

    # Calculate net salary
    net_salary = gross - deduction

    # Display salary statement
    print("\n===== EMPLOYEE SALARY STATEMENT =====")
    print("Employee Name:", name)
    print("Employee ID:", emp_id)
    print("Basic Salary: Rs.", basic)
    print("Allowances: Rs.", allowances)
    print("Overtime Pay: Rs.", overtime)
    print("Incentives: Rs.", incentives)
    print("------------------------------------")
    print("Gross Salary: Rs.", gross)
    print("Deduction Rate:", percentage, "%")
    print("Deduction Amount: Rs.", deduction)
    print("------------------------------------")
    print("Net Salary: Rs.", net_salary)
    print("====================================")
