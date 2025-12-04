import re 
url = input("Enter your twitter profile Link: ").lower().strip()
actual = re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$","",url,re.IGNORECASE)
print(actual)