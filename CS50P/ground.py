#OBJECT ORIENTED PROGRAMMING

class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} is name and {student.house} is house")


def get_student():
    data = Student
    data.name = input("Enter the name: ")
    data.house = input("Enter your house: ")
    return data 
if __name__== "__main__":
    main()

