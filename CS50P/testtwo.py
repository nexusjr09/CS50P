from testone import calculation

def main():
    checking()

def checking():
   assert calculation(2) == 4
   assert calculation(3) == 9
   assert calculation(4) == 16

if __name__ == "__main__":
    main()