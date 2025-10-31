import random

names = ["Bigyan","Aditi","Akash","Wanchhu"]
random.seed(1) #makes it consistent 
print(random.choices(names, k=2))

#remaining