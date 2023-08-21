from LoginModule import *
from StudModule import *
from AttendanceModule import *

credentials = {'student': '123', 'teacher': '12345'}
studList = {}
attendances = {}
print("Welcome to School Attendance Management!!!")

while True:
    print("1. Login")
    print("0. Exit")
    opt = input("Enter your choice: ")

    if opt == '1':
        username = input("Username: ")
        pwd = input("Password: ")
        if login(credentials,username, pwd):
            print("Login successful.")
            if username in studList:
                while True:
                    print("\n1. View My Attendance")
                    print("2. Change Password")
                    print("3. Logout")
                    action = input("Enter your action: ")

                    if action == '1':
                        roll_n = username
                        attendance_data = view_attendance(studList, attendances,roll_n)
                        for date, present in attendance_data.items():
                            status = "Present" if present else "Absent"
                            print(f"Date: {date}, Status: {status}")

                    elif action == '2':
                        change_pwd(credentials,username)  

                    elif action == '3':
                        print("Logged out.")
                        break
                    
            elif username.startswith('teacher'):
                while True:
                    print("\n1. Add Student")
                    print("2. Update Student")
                    print("3. Delete Student")
                    print("4. Mark Attendance")
                    print("5. Generate Report")
                    print("0. Logout")
                    action = input("Enter your action: ")

                    if action == '1':
                        roll_n = input("Enter Roll Number: ")
                        if roll_n in studList:
                            print("Roll number already exists.")
                        else:
                            name = input("Enter Name: ")
                            add_student(credentials,studList, attendances,roll_n, name)

                    elif action == '2':
                        roll_n = input("Enter Roll Number: ")
                        name = input("Enter Updated Name: ")
                        update_student(studList, roll_n, name)

                    elif action == '3':
                        roll_n = input("Enter Roll Number: ")
                        delete_student(studList, attendances,roll_n)

                    elif action == '4':
                        markingDate = input("Enter Date (YYYY-MM-DD): ")
                        mark_attendance(studList, attendances,markingDate)

                    elif action == '5':
                        print("1. For all Students")
                        print("2. For Single Student")
                        new_op = int(input("Enter your choice : "))
                        if new_op == 1:
                            period = input("Enter Period (daily/weekly/monthly): ")
                            generate_all_reports(studList,attendances,period)
                        
                        elif new_op == 2:
                            roll_n = input("Enter Roll Number: ")
                            period = input("Enter Period (daily/weekly/monthly): ")
                            report = generate_report(studList, attendances,roll_n, period)
                            print(report)

                        else:
                            print("Invalid option. Please select a valid option.")

                    elif action == '0':
                        print("Logged out.")
                        break

    elif opt == '0':
        print("Exited from the system!!!!")
        break

    else:
        print("Invalid choice,Please try again!!")

