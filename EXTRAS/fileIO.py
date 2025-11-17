students = []
with open ("names.csv") as file:
    for line in file:
        name,house = line.strip().split(",")
        student = {"name": name , "house": house}
        students.append(student) 

def get_name(student):
    return student["house"] 

for student in sorted(students , key = get_name):
    print(f"{ student['name'] } is from {student['house']}")      
        