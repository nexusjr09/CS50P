#OBJECT ORIENTED PROGRAMMING

def main():
    data = get_student()
    print(f"{data['name']} is name and {data['house']} is house")


def get_student():
    student = {}
    student["name"] = input("Enter your name: ")
    student["house"] = input("Enter your house: ")
    return student
if __name__== "__main__":
    main()