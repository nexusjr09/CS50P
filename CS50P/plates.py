def main():
    """Prompts the user for a plate and determines if it is valid."""
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):


    if not (2 <= len(s) <= 6):
        return False

    if not s.isalnum():
        return False

    if not s[:2].isalpha():
        return False

    first_digit_index = -1

    for i in range(len(s)):
        if s[i].isdigit():
            first_digit_index = i
            break

    if first_digit_index == -1:
        return True

    if s[first_digit_index] == '0':
        return False

    for i in range(first_digit_index, len(s)):
        if not s[i].isdigit():
            return False

    return True

if __name__ == "__main__":
    main()
