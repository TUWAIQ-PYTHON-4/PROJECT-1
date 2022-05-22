def mnue():
    '''function for print mnue to user'''
    print(
        "** WELCOME TO BAGS STORE ** \n "
        "- IF You Want to add a bags  - Enter 1 please -  \n "
        "- IF You Want to view all a bags in store - Enter 2 please - \n "
        "- IF You Want to find a bag informations - Enter 3 please - \n "
        "- IF You Want to find a bag price - Enter 4 please - \n "
        "- IF You Want to calculate bag price after discount - Enter 5 please - \n "
        "- IF You Want to Exit - Enter 6 please - ")

mnue()

def display_bags(dic_bags:dict):
    '''function for display all the bags in store'''
    for key in dic_bags.values():
        print(key)

# function to return vlue 
def find_bags(dic_bags:dict,ID_bags):
    '''function fo display bag informations the user search'''
    if ID_bags in dic_bags.keys():
        if ID_bags==ID_bags:
            return dic_bags[ID_bags]
    else:
        return "Sorry, did not find the bag"

def find_price(dic_bags:dict,ID_Bags):
    '''function for display bag price the user search'''
    if ID_Bags in dic_bags.keys():
        if ID_Bags==ID_Bags:
            print("bag price is :"+dic_bags[ID_Bags][3])
    else:
        print("Sorry, did not find the bag")

def discaont(price_bags):
    '''function for cheack if the bag Larg than 500 will calclate discount'''
    if price_bags>500:
        before_discaont= lambda price_bags : price_bags/100*50
        print("bag price after discount:")
        print(price_bags-before_discaont(price_bags))
    else:
        print("Sorry,this bag dose not include the discount")


