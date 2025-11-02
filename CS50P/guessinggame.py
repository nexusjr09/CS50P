import random 

while True:
    try:
        data = input("Level: ")
        data = int(data)
        if data > 0 :
            break
    except ValueError:
        pass
choice = random.randint(1,data)
while True:
    try:
        guess = int(input("Enter the guess: "))
        if guess > 0:
            pass
    except ValueError:
        continue 
    if guess > choice:
        print("Too large")
    elif guess < choice:
        print("Too Small!")
    else:
        print("Just Right!")
        break