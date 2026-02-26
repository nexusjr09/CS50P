def main():
    yell("this is cs50 beatchs")

def yell(words):
    uppercased = [words.upper for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()