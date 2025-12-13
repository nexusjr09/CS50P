import re
import sys


def main():
    print((convert(input("Hours: "))).lower())


def convert(s):
    pattern = r"(\d*)(:\d\d)? (\w\w) to (\d*)(:\d\d)? (\w\w)"
    if match:= re.search(pattern,s):
        start_hour = match.group(1)
        start_minute = match.group(2)
        if start_minute == "":
            start_minute = 00
        start_meridian = match.group(3)
        end_hour = match.group(4)
        end_minute = match.group(5)
        if end_minute == "":
            end_minute = 00
        end_meridian = match.group(6)
        if start_meridian == "PM" and start_hour < 12:
            start_hour = int(start_hour) + 12
            if end_meridian == "PM" and end_hour < 12:
                end_hour = int(end_hour) + 12




if __name__ == "__main__":
    main()


#9:00 AM to 5:00 PM
#9 AM to 5 PM
#9:00 AM to 5 PM
#9 AM to 5:00 PM