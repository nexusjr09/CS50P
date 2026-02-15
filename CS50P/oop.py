class Student:
    def __init__(self,house,name):
        if not name:#equals to if name ==""": 
            raise ValueError("Missing Name !")
        
        self.name = name
        self.house = house
    def __str__(self):
        return f"{self.name} is from {self.house}"
 
 
    @property
    def house(self):
        return self._house
    @house.setter
    def house(self,house):
        if house not in ["Kathmandu","Lalitpur","Bhaktapur","Chabel"]:
            raise ValueError("Invalid house location ")
        else:
            self._house = house
    
    
def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Enter the name: ")
    house = input("Enter the house: ")
    return Student(house,name)
if __name__ == "__main__":
    main()

class Student:
    
    def __init__(self,name):
        self.name = name  
        print("Dunder is here ")

s1 = Student("Bigyan")
print(s1.name)

s2 = Student("Baral")
print(s2.name)

# class Car:
#     color = "Blue"
#     model = "BMW"


# c1 = Car()
# print(c1.color)
# print(c1.model)