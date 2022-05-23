from msilib.schema import Error
import TotalAmount
class OZWater:
    
    def __init__(self, item_number: int, item_name: str, item_price:float):
        self.__item_number = item_number
        self.__item_name = item_name
        self.__item_price = item_price


    # self and get
    def set_item_number(self, item_number):
        self.__item_number = item_number
    def get_item_number(self):
        return self.__item_number
    
    def set_item_name(self, item_name):
        self.__item_name = item_name
    def get_item_name(self):
        return self.__item_name

    def set_item_price(self, item_price):
        self.__price = item_price
    def get_price(self):
        return self.__item_price

    
# added prodcuts by objects
item_1 = OZWater(1, "OZ Water 330ml", 1.00)
item_2 = OZWater(2, "OZ Water 600mL", 2.00)
item_3 = OZWater(3, "OZ Water 1L", 2.50)


cart = [] # shopping cart
price = [] # price of item
total = 0

def fun():
    back_to_main = True
    while back_to_main :
        
        print("===========================")
        print("Welcome To OZ Water Store")
        print("---------------------------")
        print("Enter [1] for show prodcuts")
        print("Enter [2] for to show shopping cart")
        print("Enter [3] for checkout")
        print("Enter [4] for contact us")
        print("Enter [5] to exit from program")
        user_input= input()  
    
        if user_input == "1":
            print("Item Number:", item_1.get_item_number()," | ", "Item Name:", item_1.get_item_name(), " | ", "Item price:", item_1.get_price())
            print("Item Number:", item_2.get_item_number()," | ", "Item Name:", item_2.get_item_name(), " | ", "Item price:", item_2.get_price())
            print("Item Number:", item_3.get_item_number()," | ", "Item Name:", item_2.get_item_name(), " | ", "Item price:", item_3.get_price())
            user_input = input("\n Do you want to Add Any of them to shopping cart? Enter 'yes' or 'no'")
            if user_input == "yes":
                user_input = input("\n Please Enter the Item Number")
                if user_input =="1":
                    cart.append(item_1.get_item_name())
                    price.append(item_1.get_price())

                elif user_input =="2":
                    cart.append(item_2.get_item_name())  
                    price.append(item_2.get_price())


                elif user_input =="3":
                    cart.append(item_3.get_item_name())
                    price.append(item_3.get_price())

                print("Added Successfully")

            elif user_input =="no":
                fun() # back to startup

        if user_input =="2":
            print(cart)

        if user_input =="3":
            for c,p in zip(cart, price):
                print(c,p, "SAR")
                temp_price = p
                global total
                total += temp_price 
            try:    
                TotalAmount.Totalfun(total) # for example if i forget import the Amount Total modules, then it will holding the error
                TotalAmount.Disount(total) # Used lambda function
            except Exception as e:
                print("somethings wrong", e)  


        if user_input =="4":
            print("Thank you for visit\n Email: info@somthing.com \n Website: www.somthing.com")
            quit() 

        if user_input =="5":
            quit()   

fun()


