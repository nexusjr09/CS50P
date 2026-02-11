class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} is from {student.house}")

def get_student():
    student = Student()
    student.name = input("Enter student name: ")
    student.house = input("Enter student house: ")
    return student    
if __name__ == "__main__":
    main()