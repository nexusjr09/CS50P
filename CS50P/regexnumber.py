import re 

data = {"+977":"Nepal", "+1":"USA","+62":"Indonesia"}
number = input("Enter the number: ")
pattern = r"\+\d{1,3} \d{3}-\d{3}-\d{4}"
if match := re.search(pattern,number):
    print("Valid !!")
else:
    print("Invalid !!")
