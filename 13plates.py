#start with 2 letters
#minimum 2 words maximum 6 (could be all letters + numbers at the end 
#numbers should only be at last 
#first number cannot be zero 
#no special characters 

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
   start_two = s[:2] 
   if len(s)>= 2 and len(s)<=6 and start_two.isalpha() and s.isalnum():    #isalnum()forspecialcharacter
       return s
main()
