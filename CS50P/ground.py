def main():
    while True:
        try:
            data = input("Fraction: ")
            result = convert(data)
            gauge(result)
            break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction):
    x_str, y_str = fraction.split("/")
    x = int(x_str)
    y = int(y_str)
    if x > y or x < 0 or y <= 0:
        raise ValueError
    return round((x / y) * 100)

def gauge(percentage):
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

if __name__ == "__main__":
    main()

    


if __name__ == "__main__":
    main()