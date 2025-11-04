def main():
   greet = input("Greeting: ")
   print(value(greet))


def value(greeting):
    processed_greeting = greeting.lower().strip()
    if processed_greeting.startswith("hello"):
        return 0
    elif processed_greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
