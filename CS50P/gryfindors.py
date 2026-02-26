students = [
    {"name":"Bigyan","home":"Lalitpur"},
    {"name":"Sandy","home":"Kathmandu"},
    {"name":"Robust","home":"Lalitpur"}
]

for student in (students):
    if student["home"] == "Lalitpur":
        print(student["name"])