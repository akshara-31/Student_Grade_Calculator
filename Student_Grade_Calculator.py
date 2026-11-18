#Student Grade Calculator
n = int(input("Enter the Number of Students: "))

for i in range(n):

    print(f"\nStudent {i+1}")

    name = input("Enter the Name of the Student: ")

    mark1 = int(input("Enter the Subject 1 Marks: "))
    mark2 = int(input("Enter the Subject 2 Marks: "))
    mark3 = int(input("Enter the Subject 3 Marks: "))
    mark4 = int(input("Enter the Subject 4 Marks: "))
    mark5 = int(input("Enter the Subject 5 Marks: "))

    if (mark1 < 0 or mark1 > 100 or
        mark2 < 0 or mark2 > 100 or
        mark3 < 0 or mark3 > 100 or
        mark4 < 0 or mark4 > 100 or
        mark5 < 0 or mark5 > 100):

        print("Invalid Marks! Enter marks between 0 and 100.")

    else:
        Total = mark1 + mark2 + mark3 + mark4 + mark5
        percentage = Total / 500 * 100

        print("\nStudent Name:", name)
        print("Total Marks:", Total, "/ 500")
        print(f"Percentage: {percentage:.2f}%")

        if (mark1 >= 35 and mark2 >= 35 and
            mark3 >= 35 and mark4 >= 35 and mark5 >= 35):

            print("RESULT: PASS")

            if percentage >= 90:
                print("GRADE: A+")
            elif percentage >= 80:
                print("GRADE: A")
            elif percentage >= 70:
                print("GRADE: B")
            elif percentage >= 60:
                print("GRADE: C")
            elif percentage >= 50:
                print("GRADE: D")
            else:
                print("GRADE: E")

        else:
            print("RESULT: FAIL")
            print("GRADE: F")
