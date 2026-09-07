#Login Validator : Check whether a username and password combination is valid.

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "password":
    print("Login successful!")
else:
    print("Invalid username or password.")