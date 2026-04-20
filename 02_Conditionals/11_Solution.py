# Nested If Conditionals Statements
# Placing one block of code inside another block of code is called nesting.

# # Login System
username = input("enter username: ")
password = input("enter password: ")

if (username == "admin" and password == "pass"):
    print("log in successful!")
else:
    if username != "admin": # NESTING
        print("wrong user name, try again.")
    else:
        print("wrong password, try again.")