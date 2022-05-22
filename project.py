


from asyncore import write
from re import I, X
from tabnanny import check
from tkinter import EXCEPTION





check:True


while check :
     
    #products in library
    products_in_shop={"python":"55 RS" , "java" :"66 RS" , "javascript" :"77 RS" , "php" :"88 RS" , ".net" :"99 RS" } #all products by using dictionary

    get_product=(products_in_shop.keys()) #to give produc "key"

    user_search = input("what do you want :") #give input from user
    key_search = "a","b","c","d" 
    if user_search not in key_search: #if user write word wrong
        try :
        # if user_search  not in key_search:
             print("please enter a to buy ")
             print("please enter b to see the list in bookstore ")
             print("please enter c to see the information about the broducts ")
             print("please enter d to exit ")
                 
        except EXCEPTION :
             print(user_search)

    if user_search == "a": #if user enter a
         user_get_product = input("what do you want to buy : ") #get proudct from the user
        #if the product we have
         if user_get_product in  products_in_shop.keys(): 
            if user_get_product == "python" :
                
                pries_of_book =input("pries of python 55 add to shooping cart ")  
                if pries_of_book == "yes" or "ok":
                  print("Purchased successfully") 
                  file = open("Purchases.txt", "w", encoding="utf-8")#write ptoduct in purchases.txt
                  file.write("python ")
                  file.close()
                  after_tax= lambda x,y:x+y
                  result =(55+15)
                  print("the price after tax ",result )
                else:#if product dom't have
                    print("the product don't hava")

            if user_get_product == "java" :
                
                pries_of_book =input("pries of java 66 add to shooping cart ")  
                if pries_of_book == "yes" or "ok":
                  print("Purchased successfully") 
                  file = open("Purchases.txt", "w", encoding="utf-8")#write ptoduct in purchases.txt
                  file.write("java ")
                  file.close()
                  after_tax= lambda x,y:x+y
                  result =(66+15)
                  print("the price after tax ",result )
            if user_get_product == "javascript" :
                
                pries_of_book =input("pries of java 77 add to shooping cart ")  
                if pries_of_book == "yes" or "ok":
                  print("Purchased successfully") 
                  file = open("Purchases.txt", "w", encoding="utf-8")#write ptoduct in purchases.txt
                  file.write("javascript ")
                  file.close()
                  after_tax= lambda x,y:x+y
                  result =(77+15)
                  print("the price after tax ",result )
            if user_get_product == "php" :
                
                pries_of_book =input("pries of java 88 add to shooping cart ")  
                if pries_of_book == "yes" or "ok":
                  print("Purchased successfully") 
                  file = open("Purchases.txt", "w", encoding="utf-8")#write ptoduct in purchases.txt
                  file.write(" php ")
                  file.close()
                  after_tax= lambda x,y:x+y
                  result =(88+15)
                  print("the price after tax ",result )
            if user_get_product == ".net" :
                
                pries_of_book =input(f"pries of .net 99 add to shooping cart ")  
                if pries_of_book == "yes" or "ok":
                  print("Purchased successfully") 
                  file = open("Purchases.txt", "w", encoding="utf-8")#write ptoduct in purchases.txt
                  file.write(" .net ")
                  file.close()
                  after_tax= lambda x,y:x+y
                  result =(99+15)
                  print("the price after tax ",result )
                
             
             
             
             
             #if the product don't have 

         elif user_get_product not in products_in_shop.keys():
            print("sorry we don't have product ")
         

#function to print the list 
    if user_search == "b":
        def list_of_pro () :  
             my_dictionary_keys_list = list(products_in_shop.keys())  
             print(my_dictionary_keys_list)
        list_of_pro()
    


    if user_search =="c":
        import user_information #class to show information about product

        
      
    if user_search == "d" :
        exit()

           



            
        
        
        
    

      











    











'''get_product_list=list(products_in_shop.keys())
search_for_product =("what buy" , get_product)
print(search_for_product)'''
