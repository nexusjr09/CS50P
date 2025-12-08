import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"(/d*)(:/d/d)? /w/w to (/d*)(:/d/d)? /w/w"
    if match:= re.search(pattern,s):
        start_hour = match.group(1)
        start_minute = match.group(2)
        end_hour = match.group(3)
        end_minute = match.group(4)
        if int(start_hour) < 12:
            int(start_hour)







if __name__ == "__main__":
    main()

#9:00 AM to 5:00 PM
#9 AM to 5 PM
#9:00 AM to 5 PM
#9 AM to 5:00 PM

#00 ---> 11 (AM)
#12 ---> 23  (PM)