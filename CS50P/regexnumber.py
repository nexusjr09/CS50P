import re 

data = {"+977":"Nepal", "+1":"USA","+62":"Indonesia"}
number = input("Enter the number: ")
pattern = r"(?P<Country_Code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
if match := re.search(pattern,number):
    print(f"The Mobile number is from: {data[match.group("Country_Code")]} ")
else:
    print("Invalid !!")
