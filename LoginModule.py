def login(credentials,username, pwd):
    if username in credentials and credentials[username] == pwd:
        return True
    return False

def set_pwd(credentials,roll_n, pwd):
    credentials[roll_n] = pwd

def change_pwd(credentials, username):
    old_pwd = input("Enter your current password: ")
    if username in credentials and credentials[username] == old_pwd:
        new_pwd = input("Enter your new password: ")
        credentials[username] = new_pwd
        print("password changed successfully.")
    else:
        print("Incorrect old password. password change failed.")

