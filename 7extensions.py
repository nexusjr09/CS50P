file_type = input("Enter your file name : ")
file_type = file_type.lower().strip()
if file_type.endswith(".gif"):
    print("image/gif")
elif file_type.endswith(".jpg"):
    print("image/jpeg")
elif file_type.endswith(".jpeg"):
    print("image/jpeg")
elif file_type.endswith(".png"):
    print("image/png") 
elif file_type.endswith(".pdf"):
    print("application/pdf")
elif file_type.endswith(".txt"):
    print("plain/txt") 
elif file_type.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")