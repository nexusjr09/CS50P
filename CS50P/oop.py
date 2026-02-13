class Student:
    def __init__(self,house,name,zodiac):
        if not name:#equals to if name ==""": 
            raise ValueError("Missing Name !")
        if house not in ["Kathmandu","Lalitpur","Bhaktapur"]:
            raise ValueError("Invalid House Name !")
        self.name = name
        self.house = house
        self.zodiac = zodiac
    def __str__(self):
        return f"{self.name} is from {self.house}"
    def charm(self):
        match self.zodiac:
            case "Piecies":
                return "🏹"
            case "Libra":
                return "🧭"
            case "Scorpion":
                return "🧪"
            case _:
                return "👺"

def main():
    student = get_student()
    print("Zodiac sign !!@!")
    print(student.charm())

def get_student():
    name = input("Enter the name: ")
    house = input("Enter the house: ")
    zodiac = input("Enter your zodiac sign: ")
    return Student(house,name,zodiac)
if __name__ == "__main__":
    main()

