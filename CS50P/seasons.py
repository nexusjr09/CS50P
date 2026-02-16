from datetime import date
import sys
import inflect



def main():
   data =  input("Enter your birthdate: ")
   conversion(data)
def conversion(x):
    try:
        birth = date.fromisoformat(x)
    except ValueError:
        sys.exit("Invalid date")
        
    today = date.today()
    if birth > today:
        sys.exit("Birth date cannot be in the future !")
    difference = today - birth 
    days = difference.days
    totalhour = days * 24
    totalminutes = totalhour * 60 
    p = inflect.engine()
    words = p.number_to_words(totalminutes,andword="")
    print(f"You have existed for total {words} Minutes in this earth !")



if __name__ == "__main__":
    main()