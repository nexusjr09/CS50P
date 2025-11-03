from testone import calculation

def main():
    checking()

def checking():
    try:
        assert calculation(2) == 4
    except AssertionError:
        print("Negative ! Not correct !")
if __name__ == "__main__":
    main()
