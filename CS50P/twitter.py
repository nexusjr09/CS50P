import re 
url = input("Enter your twitter profile Link: ").lower().strip()
actual = re.sub(r"htpps://twitter.com/","")
print(actual)