from PIL import Image

def main():
    with Image.open("costume1.png") as file:
        print(file.size)
        print(file.format)

main()