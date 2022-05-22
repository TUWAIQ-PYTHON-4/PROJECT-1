from database import *

class Delivery:

    def __init__(self, name, address, phone):
        self.name = name 
        self.address = address
        self.phone = phone



    def welcome_message(self):
        print(f"Welcome {self.name}, your address is {self.address}, your phone is {self.phone}")

    

print("Welcome to our fruit shop")
User_input = input ("To view products enter 1, to check out enter 2 : ")
def menu():
    for item in Fruits :
        print(item["id"] , "Item is: " , item["name"] , "Quantity available is: " , item["Quantity"] ,"Price is:" , item["Price"] , "SR.")

if User_input == "1" :
    menu()
else :
    exit(0)

def qty(item):
    User_input_Quantity = input("Enter Quantity for " + item["name"] + " you need: ")
    if not User_input_Quantity.isnumeric():
         print("==========================================")
         print ("Pleas enter only number or more than 0 !!! !!!")
         print("==========================================")
         qty(item)
    elif int(User_input_Quantity) > item["Quantity"] :
        print("==========================================")
        print ("The required quantity is not available !!!")
        print("==========================================")
        qty(item)
    
    else :
        item["Quantity"] = item["Quantity"]  - int(User_input_Quantity)
        
        Cart.append({
                    "id" : item["id"],
                    "name" : item["name"],
                    "Price" : item["Price"],
                    "Quantity" : int(User_input_Quantity)
                    })

def total (latestItem:list):
    sum = 0
    for items in latestItem:
        sum += items["Price"] * items["Quantity"]
    return sum

def remove_duplicated_items():   
    latest_dict = {}

    for item in Cart:
        t = item['id']
        if t not in latest_dict:
            latest_dict[t] = item
        else:
            latest_dict[t]["Quantity"] += item["Quantity"]


    latestItem = list(latest_dict.values())

    for item in latestItem:
        print("Item is: " , item["name"], ", Quantity is: ", item["Quantity"] ,", Price is:" , item["Price"] , "SR.")

    print("Total is: ", total(latestItem))

def buy () :
    answer = True
    User_input = input("Enter id for poduct you need: ")
    for item in Fruits :
        if int(User_input) == item["id"]:
            answer = False
            qty(item)

            User_input = input("Do you need another product? 1 for yes 2 for no: ")
            if(int(User_input) == 1):
                menu()
                buy()
            else:
                User_input = input("Do you want to deliver your order? 1 for yes 2 for no: ")
                if(int(User_input) == 1):
                    User_input_Name = input("Enter Your Name: ")
                    User_input_Address = input("Enter Your Address: ")
                    User_input_Phone = input("Enter Your Phone: ")
                    yourDelivery = Delivery(User_input_Name, User_input_Address, User_input_Phone)
                    yourDelivery.welcome_message()
                    print("Your invoice is : ")
                    remove_duplicated_items()
                
                    break
                else:
                    print("Your invoice is : ")
                    remove_duplicated_items()
                    
                    break

    if(answer == True):
        print("================")
        print("Wrong Enetr !!!")
        print("================")
        menu()
        buy()

try:
    buy()
except ValueError as v :
    print("Pleas enter number from the list !!!")
    buy()