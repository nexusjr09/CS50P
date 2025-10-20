texts = input("Enter String : ")
for text in texts:
    if text.isdigit():
        position = texts.index(text)
        print(position) 