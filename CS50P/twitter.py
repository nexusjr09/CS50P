import re 
url = input("Enter your twitter profile Link: ").lower().strip()
actual = re.sub(r"(https?://)?(www\.)?twitter.com/","",url)
print(actual)