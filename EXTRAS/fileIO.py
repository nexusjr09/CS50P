with open("fileIO.txt","r") as file:
    data = file.readlines()
    
for line in data:
    print("heloo", line)