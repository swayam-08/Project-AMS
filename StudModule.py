from LoginModule import set_pwd
def add_student(credentials,studList, attendances,roll_n, name):
    if roll_n in studList:
        print("Roll number already exists.")
    else:
        studList[roll_n] = name
        attendances[roll_n] = {}
        password = input("Enter a password for the student: ")
        set_pwd(credentials,roll_n, password)  
        print("Student added successfully.")


def update_student(studList,roll_n, name):
    if roll_n in studList:
        studList[roll_n] = name
        print("Student information updated successfully.")
    else:
        print("Student not found.")
def delete_student(studList, attendances,roll_n):
    if roll_n in studList:
        del studList[roll_n]
        del attendances[roll_n]
        print("Student deleted successfully.")
    else:
        print("Student not found.")
