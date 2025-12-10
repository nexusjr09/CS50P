import re
import sys


def main():
    print((convert(input("Hours: "))).lower())


def convert(s):
    pattern = r"(/d*)(:/d/d)? (/w/w) to (/d*)(:/d/d)? (/w/w)"
    if match:= re.search(pattern,s):
        start_hour = match.group(1)
        start_minute = match.group(2)
        start_meridian = match.group(3)
        end_hour = match.group(4)
        end_minute = match.group(5)
        end_meridian = match.group(6)
        





if __name__ == "__main__":
    main()
