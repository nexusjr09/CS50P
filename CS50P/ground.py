class Student:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.m1 = int(input("Enter the marks of S1: "))
        self.m2 = int(input("Enter the marks of S2"))
        self.m3 = int(input("Enter the marks of S3" ))
    def get_average(self):
        return print("The average is: ",self.m1 + self.m2 + self.m3 / 3 )
    
s1 = Student()
s1.get_average()

    