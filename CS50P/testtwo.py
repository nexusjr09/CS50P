from testone import calculation

def main():
    checking()

def checking():
    if calculation(2) != 4:
        print("wrong !")
    elif calculation(4) != 16:
        print("Wrong its 16")

if __name__ == "__main__":
    main()
