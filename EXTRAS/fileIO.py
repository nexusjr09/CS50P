for _ in range(3):
    data = input("Enter Your names: ")
    
    file = open("fileIO.txt","w")
    file.write(data)

file.close()