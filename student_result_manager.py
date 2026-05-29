student = {}

while True:
    print("\n----------------STUDENT MANAGER APP----------------")
    print("1. Add Student")
    print("2. View Student")
    print("3. Check Result")
    print("4. Exit")

    choice = input("Enter your choice: ")

    #Add Student
    if choice == '1':
        name = input("Enter student name: ")
        # roll_number = input("Enter student roll number: ")
        marks = input("Enter student marks : ")
        # marks_list = list(map(int, marks.split(',')))
        student[name] = marks
        print( f"{name} Added successfully!")  

    #view students
    elif choice == '2':
        if not student:
            print("No students found.....! ")
        else:
            for name, marks in student.items():
                print(name, ":", marks)

    #check result
    elif choice == '3':
        name = input("Enter student name: ")
        # roll_number = input("Enter student roll number: ")
        # if roll_number in student:
        #     details = student[roll_number]
        #     average_marks = sum(details['marks']) / len(details['marks'])
        #     print(f"Student Name: {details['name']}, Average Marks: {average_marks:.2f}")
        # else:
        #     print("Student not found.....! ")

        if name in student:
            marks = student[name]

            if marks >= 40:
                print(f"Student Name: {name}, Marks: {marks}, Result: Pass")
            else:
                print(f"Student Name: {name}, Marks: {marks}, Result: Fail")

        else:
            print("Student not found.....! ")

    #Exit
    elif choice == '4':
        print("Exiting the application. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
            