students = []
with open ("names.csv") as file:
    for line in file:
        name,house = line.strip().split(",")
        student = {"name": name , "house": house}
        students.append(student) 

def get_name(student):
    return student["house"] 
