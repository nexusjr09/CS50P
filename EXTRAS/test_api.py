import requests

def main():
    
    url = "https://rest.coincap.io/v3/assets?apiKey=353debcd0dbc55a8a2f151d3c6984de7d5b0a7cadb17d42a054ebf7ed3f2038b"
    
    try:
        response = requests.get(url)
        data = response.json() 
        
        # 'data["data"]' is now a list, so we loop through every coin
        for coin in data["data"]:
            name = coin["name"]
            symbol = coin["symbol"]
            
            # Some obscure coins might occasionally be missing price data
            if coin["priceUsd"]:
                price = float(coin["priceUsd"])
                print(f"1 {symbol} ({name}) is currently priced as: ${price:,.2f}")
            else:
                print(f"1 {symbol} ({name}) currently has no price data available.")
                
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    main()