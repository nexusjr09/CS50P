class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} is from {student.house}")

def get_student():
    name = input("Enter the name: ")
    house = input("Enter the house: ")
    student = Student(name,house)
    return student   
if __name__ == "__main__":
    main()