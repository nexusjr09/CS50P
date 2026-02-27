import requests

def main():
    url = "https://api.coincap.io/v2/assets/bitcoins"
    try:
        response = requests.get(url)
        data = response.json() #json format is converted to dictionary format using .json()
        price = data["bitcoin"]["usd"]
        print("1 BTC is currently priced as: $",price)
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    main()