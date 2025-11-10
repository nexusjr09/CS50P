with open("fileIO.txt") as file:
    for line in sorted(file):
        print("hello",line.rstrip())    