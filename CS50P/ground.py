#OOP IN PYTHON

def main():
    student = get_student()
    if student["name"] == "Abhishek":
        student["house"] = "Jhapa"
        print(f"{student["name"]} is from {student["house"]}")

def get_student():
    name = input("Enter the name: ")
    house = input("Enter the house: ")
    return {"name":name,"house":house}
if __name__ == "__main__":
    main()