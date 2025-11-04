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
    if len(s) >= 2 and len(s) <= 6:
        if s.isalpha():
            return True
        elif s.isalnum() and s[0:2].isalpha():
            num_started = False
            for i, char in enumerate(s):
                if char.isdigit():
                    if not num_started:
                        num_started = True
                        if char == '0':
                            return False
                    else:
                        continue
                elif num_started:
                    return False
            return True
    return False

if __name__ == "__main__":
    main()
