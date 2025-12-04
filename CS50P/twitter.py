import re 
url = input("Enter your twitter profile Link: ").lower().strip()
actual = re.sub(r"https?://twitter.com/","")
print(actual)