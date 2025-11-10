data = []

with open("fileIO.txt") as file:
    for line in file:
        data.append(line.rstrip())

for dat in sorted(data):
    print(f"Hello, {dat}")