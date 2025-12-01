import re

email = input("enter the email address: ")

if re.search(r"^.+@.+\.edu$",email):
    print("valid ")
else:
    print("Invalid")
