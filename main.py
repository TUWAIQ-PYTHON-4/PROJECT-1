
from class1 import WrongWord

def Items(name):
  return name.upper() in ["BURGER" , "FRIES" , "DRINK"]

Item = ["Burger" , "Fries" , "Drink"]

price = [10,5,3]

myOrder=[]
orderCost=[]
counter=0
total=0

print ("Welcome")
  




order = input("Do you want to Order? y/n")
if myOrder =="no":
    exit()
else :    
 print("Choose your order we have:Burger,Fries,Drink :")

nextOrder = True

while nextOrder ==True:
   TheOrder = input("Enter your choice:") 
   if TheOrder =="Burger":
     myOrder.append(Item[0])
     orderCost.append(price[0])
     counter=counter+1
     total = (lambda result: result + price[0] )
   elif  TheOrder =="Fries":
     myOrder.append(Item[1])
     orderCost.append(price[1])
     counter=counter+1
     total = (lambda result: result + price[1] )
   elif  TheOrder =="Drink":
     myOrder.append(Item[2])
     orderCost.append(price[2])
     counter=counter+1
     total = (lambda result: result + price[2] )

   else:
        if myOrder != Item:
         raise WrongWord("please fill in a valid Item")

   finished = input("are you finished ordering y/n :")
   
   if finished =="n":
    nextOrder= True
   else:
    nextOrder= False

x=0

while x < counter:
    print("Item:"+(myOrder[x]))
    print("Cost:"+str(orderCost[x]))
    x=x+1


print("The Total is :"+ str(total))    
