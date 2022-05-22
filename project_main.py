from time import sleep
from colorama import Fore
from classes import *

Worktime = {"Sunday" : "8:00 am - 12:00 am","Monday" : "8:00 am - 12:00 am","Tuesday" : "8:00 am - 12:00 am","Wednesday" : "8:00 am - 12:00 am","Thursday" : "8:00 am - 12:00 am","Friday" : "4:00 pm - 12:00 am","Saturday" : "4:00 pm - 12:00 am"}
product = products()
print(f"{Fore.CYAN}\n______________________WELCOME TO {Fore.YELLOW}Apple{Fore.LIGHTCYAN_EX}Net{Fore.CYAN}______________________\n********                                                ********\n******                                                    ******\n*****                                                      *****")
try:
    answer = ""
    try:
        input_1 = ""

        x = lambda a,b:a*b
        while answer != 0:
            
            print(f"{Fore.CYAN}--------------------------------\n1) Show products in the store.\n2) show informition of all products.\n3) Show WorkTime.\n0) Exit from the store.\n--------------------------------")
            answer = int(input("Type number of option \n:"))
            print("--------------------------------")
            
            if answer == 1:
                i = 1
                for key in product.get_name():
                    print(f"{i}- {key}")
                    i +=1
                
                answer = int(input("--------------------------------\nbuy it now by typing number of the product or \"0\" for exit\n--------------------------------\n:"))
                answer -=1
                print(f"--------------------------------\n{product.get_name()[answer]} \nTotal price included Vat 15%: {product.get_price()[answer] + x(0.15,product.get_price()[answer])} SAR\n\nare you sure you want to buy this product (1) for Yes or (0) for No\n--------------------------------")
                input_1 = int(input("Type number of option \n:"))
                
                if input_1 == 1:#COOL
                    print(f"{Fore.LIGHTRED_EX}Processing in progress...")
                    sleep(3)
                    print(f"{Fore.LIGHTGREEN_EX}***COOL*** {Fore.YELLOW} Purchased successfully.\n--------------------------------\n{Fore.CYAN}------Please rate how much you like our program, as (9) very satisfactory and (0) not satisfied at all-----")
                    input_1 = int(input(":"))
                    if input_1 >= 0 and input_1 <= 5:
                        print(f"{Fore.RED}We must get better for you \U0001F972")
                    elif input_1 > 5 and input_1 <= 9:
                        print(Fore.LIGHTGREEN_EX,"We just wanted to say thank you for your purchase. We are so lucky to have clients like you!\U0001F601")
                        exit()
                    print(f"{Fore.LIGHTRED_EX}Thank you for buying from {Fore.YELLOW}Apple{Fore.LIGHTCYAN_EX}Net{Fore.LIGHTRED_EX} come back again!!")
                    exit()
                
                elif input_1 == 0:
                    continue
                
                else:
                    raise InvalidInput("Invalid input please try again")
            
            elif answer == 2:
                product.info_products()
            
            elif answer == 3:
                for key,Value in Worktime.items():
                    print(f"{key}: {Value}")
            
            elif answer != 0:
                raise InvalidInput("Invalid input please try again")
    except InvalidInput as error :
        print(error)
except InvalidInput as error :
    print(error)