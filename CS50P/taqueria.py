data = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

storage = 0.0
while True:
    try:
        entry = input("Item: ").strip().title()
        if entry in data:
            storage += data[entry]
            print(f"Total: ${storage:.2f}")
    except EOFError:
        print(f"\nTotal: ${storage:.2f}")
        break
