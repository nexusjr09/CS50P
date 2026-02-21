# balance = 0 

# def main():
#     global balance 
#     print("Old Value for Balance: ", balance)
#     deposit(5000)
#     withdraw(1000)

# def deposit(v):
#     global balance 
#     balance += v
#     print("Now the value is ",balance)

# def withdraw(n):
#     global balance 
#     balance -= n
#     print("Now the balance is",balance)

# main()

def meow(n: int)-> None:
    return "Meow/n" * n

"""Meow function documnetaion. """

number: int = int(input("Enter the number of Times:" ))
meow(number)
