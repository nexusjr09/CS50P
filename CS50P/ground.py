import re

email = input("enter the email address: ")

if re.search(r"^\w+@\w+\.(edu|com|exe)$",email,re.IGNORECASE):
    print("valid ")
else:
    print("Invalid")
