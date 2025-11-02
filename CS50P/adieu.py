import inflect
total = []
p = inflect.engine()
while True:
    try:
        data = input("Enter the Name: ")
        total.append(data)
    except EOFError:
        break
print()
print("Adieu, adieu, to", p.join(total))
