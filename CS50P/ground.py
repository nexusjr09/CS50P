#OBJECT ORIENTED PROGRAMMING

class Student:
    def __init__(self,name,house):
        if not name:
            return ValueError("Missing Name")
        if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house



def main():
    student = get_student()
    print(f"{student.name} is name and {student.house} is house")


def get_student():
    name = input("Enter your name: ")
    house = input("Enter your house : ")
    data = Student(name,house)
    return data 
if __name__== "__main__":
    main()

