correct_user = "admin"
correct_pass = "1234"

user = input("Enter username: ")
pwd = input("Enter password: ")

if user != correct_user:
    print("Invalid Username")
elif pwd != correct_pass:
    print("Invalid Password")
else:
    print("Login Successful")