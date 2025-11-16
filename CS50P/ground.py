with open ("names.csv") as file:
    for line in file:
        dat = line.strip().split(",")
        print