import re

email = input("enter the email address: ")

if re.search(r"^[a-zA-Z]+@[A-Za-z]+\.edu$",email):
    print("valid ")
else:
    print("Invalid")
