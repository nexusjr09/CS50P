import re 

user_input = input("Enter the hash Code: ")

pattern = r"^#[a-f]{6}$"
result = re.search(pattern,user_input)
if result:
    print(f"It is Valid and its result is: {result.group()}")
else:
    print("invalid pattern")