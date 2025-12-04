import re 
url = input("Enter your twitter profile Link: ").lower().strip()
if actual := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)",url,re.IGNORECASE):
    print(f"Username: {actual.group(1)}")