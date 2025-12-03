name = input("Enter your full name: ")
if "," in name:
    last,first = name.split(", ")
    name = f"{first} {last}"
    print(f"Hello {name}")
else:
    print(f"Hello {name}")