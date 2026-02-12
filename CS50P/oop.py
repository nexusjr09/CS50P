class Student:
    def __init__(self,house,name):
        if not name:#equals to if name ==""": 
            raise ValueError("Missing Name !")
        if house not in ["Kathmandu","Lalitpur","Bhaktapur"]:
            raise ValueError("Invalid House Name !")
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} is from {student.house}")

def get_student():
    name = input("Enter the name: ")
    house = input("Enter the house: ")
    return Student(house,name)
if __name__ == "__main__":
    main()

