import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(:\d{2})? (AM|PM) to (\d{1,2})(:\d{2})? (AM|PM)$"
    match = re.search(pattern, s)

    if not match:
        raise ValueError

    start_hour = int(match.group(1))
    start_minute = match.group(2)
    start_minute = int(start_minute[1:]) if start_minute else 0
    start_meridian = match.group(3)

    end_hour = int(match.group(4))
    end_minute = match.group(5)
    end_minute = int(end_minute[1:]) if end_minute else 0
    end_meridian = match.group(6)

    if not (1 <= start_hour <= 12 and 0 <= start_minute <= 59):
        raise ValueError
    if not (1 <= end_hour <= 12 and 0 <= end_minute <= 59):
        raise ValueError

    if start_meridian == "AM":
        if start_hour == 12:
            start_hour = 0
    else:
        if start_hour != 12:
            start_hour += 12

    if end_meridian == "AM":
        if end_hour == 12:
            end_hour = 0
    else:
        if end_hour != 12:
            end_hour += 12

    return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"


if __name__ == "__main__":
    main()
