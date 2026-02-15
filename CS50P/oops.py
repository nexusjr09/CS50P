class Student:
    def __init__(self,firstname,lastname,age):
        self.name = firstname
        self.lname = lastname 
        self.age = age 
        print("All data created !")

s1 = Student("Bigyan","Baral","18")
print(s1.name)
print(s1.lname)
print(s1.age)

s2 = Student("Amrit","Subba","19")
print(s2.name)
print(s2.lname)
print(s1.age)