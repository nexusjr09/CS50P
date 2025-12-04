import re 

name = input("Enter your full name: ").strip()
if matches := re.search(r"^(.+), ?(.+)$",name): #:= walrus operator
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello {name}")