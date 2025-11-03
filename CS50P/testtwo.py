from testone import calculation

def main():
    checking()

def checking():
   try:
      assert calculation(2) == 4
      assert calculation(3) == 9
      assert calculation(4) == 16
   except AssertionError:
       print("Invalid logic")


if __name__ == "__main__":
    main()