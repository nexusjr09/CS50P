#OBJECT ORIENTED PROGRAMMING

class Student:
    def __init__(self,name,house,patronus):
        if not name:
            return ValueError("Missing Name")
        if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
         return f"{self.name} is from {self.house}"
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🏹"
            case "Otter":
                return "🔴"
            case _:
                return "💉"


def main():
    student = get_student()
    print("Patronus: ")
    print(student.charm())
def get_student():
    name = input("Enter your name: ")
    house = input("Enter your house : ")
    patronus = input("Enter your patronus: ")
    data = Student(name,house,patronus)
    return data 
if __name__== "__main__":
    main()
