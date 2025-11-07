for _ in range(3):

    data = input("Enter Your names: ")
    
    with open("fileIO.txt","a") as file:
        file.write(f"{data}\n")
