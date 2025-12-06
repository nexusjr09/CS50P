import re
import sys


def main():
    ip_adress = input("Enter your ipv4 adress: ")
    print(validate(ip_adress))


def validate(ip):
    pattern = r"^\d{0,255}\.\d{0,255}\.\d{0,255}\.\d{0,255}$"
    if match :=re.search(pattern,ip):
        return("Valid")
    else:
        return("Invalid")



if __name__ == "__main__":
    main()