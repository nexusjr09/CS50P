import re

email = input("enter the email address: ")

if re.search(r"^[a-zA-Z]+@[A-Z0-9]+\.(edu|com|exe)$",email):
    print("valid ")
else:
    print("Invalid")
