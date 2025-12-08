import re 

html_data = input("Enter the links: ")
pattern = r'^src="(https?://(?:www\.)youtube\.com/embed/[a-zA-Z_-]+)"$'
if match := re.search(pattern,html_data):
    print(match.group(1))
else:
    print("Invalid")