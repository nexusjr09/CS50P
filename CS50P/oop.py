#OOP IN PYTHON

def main():
    name = get_name()
    house = get_house()
    print(f"{name} is from {house}")

def get_name():
    return input("Enter your name: ")
def get_house():
    return input("Enter your house: ")

if __name__ == "__main__":
    main()