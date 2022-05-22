# Final update


from datetime import date
print('''

************ WORLD OF TECHNOLOGY STORE***************

Welcome to the world of Technology store

You can find more information about our products

''')
print("*****************************************")
print("")



print("Summary for our products: ")



while True:
    print("Choose the type of product [phone],[cover],[chargers] write without brackets ")
    type_prodects=input("Write here: ")

    if type_prodects =='phone' or type_prodects=='cover' or type_prodects =='chargers':
        break
    
# modules____@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#lists ______@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
if type_prodects=='phone':
    import proPhone
    print(proPhone.get_proPhone(1))
    print(proPhone.products_phones)
    
            

elif type_prodects=='cover':
    import proCovers
    print(proCovers.get_proCovers(1))
    print(proCovers.products_covers)

elif type_prodects=='chargers':
    import proCharger
    print(proCharger.get_proCharger(1))
    print(proCharger.products_chargers)




print("Do you need more details?[yes]or[no]to exit?")
aaa=input("Enter here: ")
if aaa=='yes':
    print(
        '''
Write  the number for product you need:
     1 - Mobile phones
     2 - Accessories and covers
     3 - chargers phones        
        '''
    )
    # Error Handling ________@@@@@@@@@@@@@@@@@@@@
    try:
        bbb=int(input("Enter here: "))
    except ValueError:
        print("please enter Integer number............")
    if bbb==1:
     #classes ---------@@@@@@@@@@@@@@@@@@@@@@@@
        class Phone:
            def __init__(self,name,price,memory,color) :
                self.nname=name
                self.pprice=price
                self.mmemory=memory
                self.ccolor=color
            def phone_det(self):
                    return f"{self.nname} {self.pprice} {self.mmemory} {self.ccolor}"
        iphone_pr=Phone('iphone 13','price=4500 SAR','memory is 265 G','color is Black')
        galaxy_pr=Phone('galaxy s22','price=3680 SAR','memory is 512 G','color is Red')
        huawei_pr=Phone('huawei p40','price=4000 SAR','memory is 512 G','color is Red')

        while True:
            print('''Enter the company of product same laters without brackets:
       [apple],[galaxy],or[huawei]

       if have error please write again


        ''')
            cc=input("Enter here: ")
            if cc=='apple' or cc=='galaxy' or cc=='huawei':
                break
        if cc=='apple':
            iphone=iphone_pr.phone_det()
            print(iphone)
        
        elif cc=='galaxy':
            galaxy=galaxy_pr.phone_det()
            print(galaxy)
        elif cc=='huawei':
            huawei=huawei_pr.phone_det()
            print(huawei)

    elif bbb==2:
        phone_covers={'iphone cover':'150 SAR','galaxy cover':'120SAR','huawei cover':'145 SAR'}
        print(phone_covers)
    elif bbb==3:
        chrgers={'iphone charger':'350 SAR','galaxy charger':'280 SAR','huawei charger':'225 SAR'}



#@@@@@@@@@@@@@______________@@@@@@@@@__________

print("do you want to buy? y or n for exit....")

qus_ff=input()

if qus_ff == 'y':
    items = {}
    print("To start shopping, note down what you want to buy and how much of it")
    print("Here are the purchasable items")
    print("~~~~~")
    print("12345670 is a ipone13 (4500 SAR)")
    print("12345671 is a galaxy s22 (3680 SAR)")
    print("12345672 is a huawei p40 (4000 SAR)")
    print("12345673 is iphone cover (150 SAR)")
    print("12345674 is a galaxy cover (120 SAR)")
    print("12345675 is huawei cover (145 SAR)")
    print("12345676 is iphone charger (350 SAR)")
    print("12345677 is a galaxy charger (280 SAR)")
    print("12345678 is huawei charger (225 SAR)")
    print("~~~~~")
    #dictionary _________@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    possibleOrders = {'12345670' : {'name' : 'ipone13', 'price' : 4500},
         '12345671' : {'name' : 'galaxy s22', 'price' : 3680},
         '12345672' : {'name' : 'huawei p40', 'price' : 4000},
         '12345673' : {'name' : 'iphone cover', 'price' : 150},
         '12345674' : {'name' : 'galaxy cover', 'price' : 120},
         '12345675' : {'name' : 'huawei cover', 'price' : 145},
         '12345676' : {'name' : 'iphone charger', 'price' : 350},
         '12345677' : {'name' : 'galaxy charger', 'price' : 280},
         '12345678' : {'name' : 'huawei charger', 'price' : 225}}
    print("Alright, now start typing what you want to order")
    print(" ")
    price = 0
    full_list = " "
    chos_items = []
    while full_list != "":
        print(" ")
        full_list = input("Type: ")
        if full_list == 'end':
            break
        item = int(full_list)
        amount = int(input("Amount: "))
        item = int(full_list)

        if full_list in possibleOrders:
            orders = print("{}    {:>5}    (SAR{:0.2f})".format(full_list,     possibleOrders[full_list]['name'], possibleOrders[full_list]['price']))
            if orders != "":
                chos_items.append(full_list)
            price  = int(amount) * (possibleOrders[full_list]['price']) + price
            print("Subtotal is currently at "+str(price))
            print("if you need bey more write the sequnce number or end to finsh....")

    print("Your subtotal is: " +str(price))
    while True:
        print("Do you want to complete the purchase??[y>>yes,n>>no,exit]")
        print("if you finsh write 'n' to save your info... ")
        f_qus=input()
        if f_qus == "y":
            print('''
         What is  your name ?
         What is your E-mail address?
         What is your Phone number?
         write your Address?
         ''')
            list=[]
            n = 4
            for aa in range(0,n):
                ele = (input())
                list.append(ele)
                print(list)
                with open('info.txt', 'w') as f:
                    for item in list:
                        f.write("%s\n" % item)


        elif f_qus=='n':
            print(": do you want to list your informations ?[y>>yes,n>>no,exit]")
            second_qus=input()
            if second_qus=="y":
                a_file = open("info.txt")
                lines = a_file.readlines()
                for line in lines:
                    print(line)
                    break 
            elif second_qus=='n':
                break
            elif second_qus=="exit":
                break
        
    #----------------------------------------------
    print("________________world of Technology________________")
    today = date.today()
    print("Today's date:", today)
    print("Thank you  ",list[0])
    print("**************")
    t=price*0.15
    
    # Lamda_________@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    funtaxation = lambda t,price: t+price
    r= funtaxation(t,price)


    print(" The cost of your purchases with taxation:  ",r," __SAR")

    print("__________________")

    print("Thank you for your visit ")
    print("see you soon")
    print("To communicate: +96660003745454")


elif qus_ff=='n':
    print("Exit.....")
    print("Thank you for your visit ")
    print("see you soon")
    print("To communicate: +96660003745454")

#----------------------------------------------








