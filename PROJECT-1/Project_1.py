from re import I
#from classes import *



Dicts_brand = {'1' :"zara", 
           '2' :"adidas" , 
           '3' :"nike", 
           '4' :"gucci",
           '5' :"1902",}

i=0
while  i<1 :
    for key, value in Dicts_brand.items():
      print(key, value)
    brand_input=input("Choose the brand number:")

    if brand_input in Dicts_brand:
      print(Dicts_brand.get(brand_input))
      i=+1
    elif  not brand_input.isalnum:
     print("This is invalid number")   
    else:
       print("Sorry, the number is not found")


brand = {'1' :"Short", 
           '2' :"Shoe" , 
           '3' :"Shirt", 
           '4' :"T-shirt", 
          '5' :"Hat",}
i=0
while  i<1 :  
    for key, value in brand.items():
           print(key, value)
    in_put=input("enter the:")
    if in_put in brand:
         print(brand.get(in_put))
         i=+1
    elif  not in_put.isalnum:
         print("This is invalid number")              
    else:
          print("Sorry, the number is not found")



asn=in_put 
asn2=in_put

price_Short=150
price_Shoe=300
price_Shirt=99
price_T_shirt=99
price_Hat=50

if asn ==  '1':
    size_Short=input("Enter your size M,L,XL,XXL:")
    if size_Short == "m" or size_Short == "l" or size_Short == "xl" or size_Short == "xxl"or size_Short == "M" or size_Short == "L" or size_Short == "XL" or size_Short == "XXL":
     print(size_Short,"Price")
     price=lambda tax :price_Short*0.15+price_Short
     print(price(tax=price_Short))
    else:
        print("The wrong size")


if asn2 == '2':
    size_Shoe=input("Enter your size 39,40,41,42:")
    if size_Shoe == "39" or size_Shoe == "40" or size_Shoe == "41" or  size_Shoe =="42" or size_Shoe == "43" or  size_Shoe =="44":
       print(size_Shoe,"Tm2")
       price=lambda tax :price_Shoe*0.15+price_Shoe
       print(size_Shoe,"Price is", price(tax=price_Shoe))
    else:
        print("The wrong size")



if asn =='3':
    size_Shirt=input("Enter your size M,L,XL,XXL:")
    if size_Shirt == "m" or size_Shirt == "l" or size_Shirt =="xl" or size_Shirt =="xxl":
     price=lambda tax :price_Shirt*0.15+price_Shirt
     print(size_Shirt,"Price is",price(tax=price_Shirt))
    else:
        print("The wrong size")


if asn =='4':
    size_T_shirt=input("Enter your size M,L,XL,XXL:")
    if size_T_shirt == "m" or size_T_shirt == "l" or size_T_shirt == "xl"  or size_T_shirt =="xxl":
        price=lambda tax :price_T_shirt*0.15+price_T_shirt
        print(price(tax=price_T_shirt))
    else:
        print("The wrong size")


if asn =='5':
     size_Hat=input("Enter your size 6,7,8,9:")
     if size_Hat =="7"or size_Hat=="8"or size_Hat== "9"or size_Hat== "10":
       price=lambda tax :price_Hat*0.15+price_Hat
       print(price(tax=price_Hat))
     else:
        print("The wrong size")

def Tnx():
    print("Thank you for using")

Tnx()
     
try:
    size_Short
except Exception as e:
    print("Error")       


