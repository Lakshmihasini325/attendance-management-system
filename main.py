students = {}

while True:
    print("\n--- Attendance Management System ---")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Save Attendance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students[name] = "Absent"
        print("Student added!")

    elif choice == "2":
        name = input("Enter student name: ")

        if name in students:
            students[name] = "Present"
            print("Attendance marked!")
        else:
            print("Student not found!")

    elif choice == "3":
        print("\nName\tAttendance")

        for name, status in students.items():
            print(name, "\t", status)

    elif choice == "4":
        file = open("attendance.txt", "w")

        for name, status in students.items():
            file.write(name + " - " + status + "\n")

        file.close()
        print("Attendance saved!")

    elif choice == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
