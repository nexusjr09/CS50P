class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass #__ is written to make it private , this value cannot be accesed outside the class

    def resetpass(self):
        print(self.acc_pass)

d1 = Account("6767","abcdich")
print(d1.acc_no)
#print(d1.acc_pass) #cannot be accessed as it is outside the class 
