def main():
    dollars = input("How much was the meal? ")
    percent = input("What percentage would you like to tip? ")
    dollars = dollars.replace("$", "")
    percent = percent.replace("%", "")
    dollars = float(dollars)
    percent = float(percent) / 100
    tip = dollars * percent
    print(f"Your tips will be  ${tip}")


main()
