

students = []
eligible = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of student", i + 1)

    name = input("Enter student name: ")
    aggregate = float(input("Enter aggregate marks: "))

    print("Enter marks in 3 subjects:")
    s1 = int(input("Subject 1: "))
    s2 = int(input("Subject 2: "))
    s3 = int(input("Subject 3: "))

    attendance = float(input("Enter attendance: "))
    income = float(input("Enter family income: "))

    students.append((name, aggregate, s1, s2,
                     s3, attendance, income))

    # Eligibility checking
    if (aggregate >= 75 and s1 >= 60 and
        s2 >= 60 and s3 >= 60 and
        attendance >= 75 and income <= 200000):

        eligible.append((name, aggregate,
                         attendance, income))
    else:
        print(name, "is Not Eligible")

# Ranking students
eligible.sort(key=lambda x: (-x[1], -x[2], x[3]))

print("\n===== SCHOLARSHIP RANKING =====")

if len(eligible) == 0:
    print("No students are eligible for scholarship.")
else:
    rank = 1

    for student in eligible:
        print("\nRank:", rank)
        print("Name:", student[0])
        print("Aggregate Marks:", student[1])
        print("Attendance:", student[2])
        print("Family Income:", student[3])
        print("Status: Eligible")
        rank += 1

print("\nProgram Completed")

