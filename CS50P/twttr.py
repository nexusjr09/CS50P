texts = input("Enter Strings : ").strip()
toremove = ["a","e","i","o","u","A","E","I","O","U"]
clean = ""
for  i in range(len(texts)):
    if texts[i]  in toremove:
        texts.replace(texts[i],"")
    else:
        clean = clean + texts[i]

print(clean)

###ANOTHER LOGICAL WAY:

texts = input("Enter Strings : ").strip()
toremove = ["a","e","i","o","u","A","E","I","O","U"]
clean = ""
for  i in range(len(texts)):
    if texts[i] not in toremove:
        clean = clean + texts[i]
print(clean)    