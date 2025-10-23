def main():
    while True:
     try:
        data = input("Fraction: ")
        result = second(data)
        if result <= 1:
            print("E")
        elif result >= 99:
            print("F")
        else:
            print(f"{result}%")
        break
     except (ValueError,ZeroDivisionError):
        pass
def second(s):
    x_str,y_str= s.split("/")
    x = int(x_str)
    y = int(y_str)
    if x > y:
       raise ValueError
    elif x < 0:
       raise ValueError
    elif y == 0:
       raise ZeroDivisionError
    else:
       calc = round(float((x / y)* 100))
    return calc

main()
