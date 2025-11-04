from test_one import calculation

def main():
    test_checking()

def test_checking():
   
      assert calculation(2) == 3 + 1
      assert calculation(3) == 9
      assert calculation(4) == 16

if __name__ == "__main__":
    main()

#WHILE USING PYTEST FUNCTION NAME SHOULD ALWAYS START WITH: test_