import re

email = input("enter the email address: ")

if re.search("*.@.*",email):
    print("valid ")
else:
    print("Invalid")
