import requests
import sys
import json

if len(sys.argv)==2:
    try:
        data = float(sys.argv[1])
        fetched = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=0b5571833597939cd4ba9fec50cdf6dd6ed7c80a4c769d4d11e7f92af4d6c37a")
        final = fetched.json()
        price = float(final["data"]["priceUsd"])
        total = data * price
        print(f"${total:,.4f}")
    except requests.RequestException:
        sys.exit("Error fetching Bitcoin Price!)")
    except ValueError:
        sys.exit("Invalid Argument")
else:
    sys.exit("Invalid command-line argument!")
