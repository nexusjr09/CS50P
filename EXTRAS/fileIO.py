students = []
with open ("names.csv") as file:
    for line in file:
        dat = line.strip().split(",")
        print(f"{dat[0]} is from {dat[1]}")
        