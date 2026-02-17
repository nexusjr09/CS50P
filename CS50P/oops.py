class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def resetpass(self):
        print(self.acc_pass)

d1 = Account("6767","abcdich")
print(d1.acc_no)
