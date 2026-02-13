class Student:
    def __init__(self,house,name):
        if not name:#equals to if name ==""": 
            raise ValueError("Missing Name !")
        if house not in ["Kathmandu","Lalitpur","Bhaktapur"]:
            raise ValueError("Invalid House Name !")
        self.name = name
        self.house = house
    def __str__(self):
        return f"{self.name} is from {self.house}"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Enter the name: ")
    house = input("Enter the house: ")
    return Student(house,name)
if __name__ == "__main__":
    main()

