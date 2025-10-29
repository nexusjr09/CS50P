data = {
    "January":"01",
    "February":"02",
    "March":"03",
    "April":"04",
    "May":"05",
    "June":"06",
    "July":"07",
    "August":"08",
    "September":"09",
    "October":"10",
    "November":"11",
    "December":"12"
}
while True:
    user = input("Enter date: ").strip()
    try:

        m, d, y = None, None, None

        if "/" in user:

            month_str, day_str, year_str = user.split("/")


            m = int(month_str)
            d = int(day_str)
            y = int(year_str)

        elif "," in user:

            parts = user.replace(",", "").split()

            if len(parts) != 3:
                raise ValueError

            month_name, day_str, year_str = parts[0], parts[1], parts[2]

            if month_name not in data:
                raise ValueError


            m = int(data[month_name])
            d = int(day_str)
            y = int(year_str)

        else:
            continue

        if not (1 <= m <= 12 and 1 <= d <= 31):
            continue

        # Final formatting
        mm = str(m).zfill(2)
        dd = str(d).zfill(2)

        print(f"{y}-{mm}-{dd}")
        break

    except (ValueError, IndexError, KeyError):
        continue
