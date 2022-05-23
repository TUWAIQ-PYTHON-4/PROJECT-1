
from pip import main


import code
def Totalfun(total): # return Total Amount
    print("Total Amount =", total, "SAR")

def Disount(total): # return Total Amount after discount 10%
    x = lambda a: total *0.90
    print("Total Amount After Discount 10% =:",x(total))
    print()
