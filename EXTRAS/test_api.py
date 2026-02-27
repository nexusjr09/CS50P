import requests

def main():
    coin_input = input("Enter coin name or symbol (e.g., bitcoin, BTC): ").lower()
    url = "https://rest.coincap.io/v3/assets?apiKey=353debcd0dbc55a8a2f151d3c6984de7d5b0a7cadb17d42a054ebf7ed3f2038b"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        found = False
        for coin in data["data"]:
            # Compare with name or symbol in lowercase
            if coin_input == coin["id"].lower() or coin_input == coin["symbol"].lower():
                price = float(coin["priceUsd"])
                print(f"1 {coin['symbol']} ({coin['name']}) is currently: ${price:,.2f}")
                found = True
                break
        
        if not found:
            print(f"Coin '{coin_input}' not found.")
                
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    main()