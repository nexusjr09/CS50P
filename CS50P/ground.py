class Account:
    def __init__(self):
        self.balance = int(input("Input your Total Balance: "))
        self.account = int(input("Please Enter your Account no: "))
        data = input("Credit or Debit").lower()
        if data == "credit":
            self.credit()

    def credit(self):
        amount = int(input("Amount to be Credited: "))
        self.balance = self.balance + amount
        print("Final Balance is",self.balance)

s1 = Account()