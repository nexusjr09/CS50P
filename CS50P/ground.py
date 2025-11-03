import random 
def main():
    data = int(input("Enter the nUmber: "))
    generate(data)
    print("Your final Output is: " ,generate(data) + data)
def generate(n):
    mess = random.randint(0,100)
    return mess
