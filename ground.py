while True:
    try:
        x = int(input("Enter the Value : "))
    except ValueError:
        print("It is not an Integer")
    else:
        break
print(f"x is {x}")