grocery = {}

while True:
    try:
        data = input()
        datmod = data.strip().upper()
        grocery[datmod] = grocery.get(datmod, 0) + 1
    except EOFError:
        for item in sorted(grocery.keys()):
            print(f"{grocery[item]} {item}")
        break
