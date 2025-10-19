texts = input("Enter your string : ").lower()
toremove = ["a","e","i","o","u"]
clean = ""
for i in range(len(texts)):
    if i in toremove:
        clean = clean + texts.replace(i,"")
    else:
        texts = clean
print(clean)