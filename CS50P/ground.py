#OOP IN PYTHON

def main():
    student = get_student()
    if student["name"] == "Abhishek":
        student["house"] = "Jhapa"
        print(f"{student["name"]} is from {student["house"]}")
