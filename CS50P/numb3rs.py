import re
import sys


def main():
    ip_adress = input("Enter your ipv4 adress: ")
    print(validate(ip_adress))


def validate(ip):
    parts = ip.split(".")
    #REGEX  PATTERN WILL  BE TOO COMPLEX SO WE USED THIS NORMAL METHOD WHICH WAS ALLOWED
    if len(parts) != 4:
        return False

    for p in parts:
        if not p.isdigit():
            return False
        if not 0 < int(p) <= 255:
            return False

    return True

if __name__ == "__main__":
    main()