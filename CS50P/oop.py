#OBJECT ORIENTED PROGRAMMING

class Student:
    def __init__(self,name,house):
        if not name:
            return ValueError("Missing Name")
        self.name = name
        self.house = house
    def __str__(self):
        return f"{self.name} is from {self.house}"
    def house(self):
        return self.house
    def house(self,house):
        if house not in ["Gryffindor","HufflePuff","Ravenclaw"]:
            raise ValueError("Invalid House")
        self.house = house
    


def main():
    student = get_student()
    student.house = "Ilam, Suryodaya Na Pa "
    print(student)
def get_student():
    name = input("Enter your name: ")
    house = input("Enter your house : ")
    data = Student(name,house)
    return data 
if __name__== "__main__":
    main()
 