#unpacking in python
def total(galleons,sickles,knuts):
    return (galleons * 17 + sickles) * 29 + knuts
coins = [100,50,25]
print(total(*coins)) # star (*) unpacks the list and sends three individual values . 