url = input("Enter your twitter profile Link: ").lower().strip()
actual = url.removeprefix("https://twitter.com/","")
print(f"Username: {actual}")