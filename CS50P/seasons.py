from datetime import date
import sys
import inflect

def main():
    data = input("Birth Date: ")
    print(convert(data))

def convert(s):
    try:
        birth = date.fromisoformat(s)
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()
    
    difference = today - birth
    minutes = difference.days * 24 * 60
    
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")
    return f"{words.capitalize()} minutes"

if __name__ == "__main__":
    main()