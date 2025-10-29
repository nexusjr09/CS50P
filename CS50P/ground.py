import cowsay
import sys
import requests

data = requests.get("https://github/" + sys.argv[1])
print(data.json)