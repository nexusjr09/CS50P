#OOP IN PYTHON

def main():
    var1,var2 = get_student()

    print(f"{var1} is from {var2}")

def get_student():
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    return name,house
if __name__ == "__main__":
    main()