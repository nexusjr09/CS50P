def main():
    data = input("Enter teh string: ").strip()
    print(shorten(data))

def shorten(word):
    toremove = ["a","e","i","o","u","A","E","I","O","U"]
    clean = ""
    for i in range(len(word)):
        if word[i] not in toremove:
            clean = clean + word[i]
            
    return clean 
        
if __name__ == "__main__":
    main()