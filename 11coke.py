amount = 0
coins = [5, 10, 25]

while amount < 50:
    print(f"Amount Due: {50 - amount}")
    coin = int(input("Insert Coin: "))
    if coin in coins:
        amount += coin
    else:
        print("Enter coin in this denominations: 5, 10, or 25")
else:
    print(f"Change Owed: {amount - 50}")
