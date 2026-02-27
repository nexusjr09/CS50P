import cowsay
import sys
import requests
import json

data = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])


raw = data.json()
for r in raw["results"]: 
    print(r["trackName"])