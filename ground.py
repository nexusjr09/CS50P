data = {"Bigyan":"110",
        "Avash":"120",
        "Alish":"130 M",
        "Milan":"150 KM"    
}
try:
    x = input("Enter the Value : ")
    rata = data[x]
    output = print(int(rata) * 5 )
except KeyError:
    print("Entered data is not stored in Dict ! ")
except ValueError:
    final = data[x]
    result = final.replace(final[-2:],"").strip()
    print(int(result) * 5)
