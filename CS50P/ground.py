import cowsay
import sys
import requests
import json

data = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(data.json(), indent=2))