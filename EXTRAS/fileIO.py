students = []

with open("names.csv") as file:
    for line in file:
        name,address = line.rstrip().split(",")
        student = {"name": name , "address": address}
        students.append(student)

for work in sorted(students, key=lambda data: data["address"]):
    print(f"{work['name']} is his name and {work['address']}")


    