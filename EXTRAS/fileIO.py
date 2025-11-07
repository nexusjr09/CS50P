for _ in range(3):
    data = input("Enter Your names: ")
    
    file = open("fileIO.txt","a") #a = append
    file.write(data)
    print()

file.close()