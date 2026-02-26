# #unpacking in python
# def total(galleons,sickles,knuts):
#     return (galleons * 17 + sickles) * 29 + knuts
# coins = {"galleons":100, "sickles": 50 , "knuts":25}
# #print(total(*coins)) # star (*) unpacks the list and sends three individual values [FOR THE LIST].
# # FOR THE DICTIONARIES YOU use two stars (**coins) 
# #print(total(galleons = 100,sickles = 50 , knuts= 25))
# print(total(**coins))  

def f(*args,**kwargs):
             print("Positional",args)
f(100,50,25)