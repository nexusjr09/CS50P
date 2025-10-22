try:
    data = int(input("Enter a string : "))
except ValueError:
    print("It's not integer")
else:
    print(data)