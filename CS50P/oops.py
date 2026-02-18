class Car:
    cc = "250"
    color = "black"
    engine = "high"
    @staticmethod 
    def start():
        print("Car started !")

    @staticmethod
    def stop():
        print("Car stopped !")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")
print(car1.stop())
print(car1.color)
print(car1.engine)
print(car1.cc)

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

c3 =Fortuner("Blackish")
print(c3.color)
print(c3.cc)