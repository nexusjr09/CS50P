#OBJECT ORIENTED PROGRAMMING

def main():
    data = get_student()
    print(f"{data[0]} is name and {data[1]} is house")


def get_student():
    name = input("Enter the name: ")
    house = input("Enter the house: ")
    return (name,house)

if __name__== "__main__":
    main()