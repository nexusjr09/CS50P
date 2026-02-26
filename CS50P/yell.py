def main():
    yell("this is cs50 beatchs")

def yell(words):
    uppercased = map(str.upper,words)
    print(*uppercased)

if __name__ == "__main__":
    main()