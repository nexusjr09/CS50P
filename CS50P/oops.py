class Student:
    college_name = "Everland Int"
    #default constructors 
    def __init__(self):
        pass
    #parameterized constructors
    def __init__(self):
        firstname = input("Enter name: ")
        lastname = input("Enter the last name: ")
        age = input("Enter the age of s1:  ")
        
        self.name = firstname #obj attri > class atri
        self.lname = lastname 
        self.age = age 
        print("All data created !")

s1 = Student()
print(s1.name)
print(s1.lname)
print(s1.age)

s2 = Student()
print(s2.name)
print(s2.lname)
print(s2.age)

 