#import Plant class module. 
from plant_class import *

#import invalidInput error module from Exception package.
from Exceptions.invalidInput import *

# creat object.
plant_1 = Plant()

print("--------------------------------")
print("Wellcome to the PLANTI store")
print("--------------------------------\n")

# while loop to interactive with users.
check = True 
while check:

    #print all services.
    print("--------------------------------")
    print("1) Show all plants in the store.")
    print("2) Informition of the plants.")
    print("3) Add plant in Shopping cart.")
    print("4) Print my receipt.")
    print("5) Exit from the store.\n")
    print("--------------------------------")    
    
    # for check if it error input or not.
    try:
        #take value from the user.
        user_input_1 = input("Type the number of the service you want: ")
         # if user choose number 1.
        if user_input_1 == "1":
            print("________________________________")
            print("          PLANTS NAMES          ")
            print("________________________________")
            cont = 1
            # to print all names of plants.
            # first check if there is any plans in store.
            if len(plant_1.get_name()) != 0:
                for plant in plant_1.get_name():
                    print(f"      {cont}: {plant}")
                    cont +=1

            # if no plant in stor.
            else:
                print("Sorry there are no items in store \"COMMING SOON\"")
            print("________________________________")

        # if user choose number 2.
        elif user_input_1 == "2":

            #call function fron class "Plant" to print all informations of plants.
            plant_1.info_plants()
        
        # if user choose number 3.
        elif user_input_1 == "3":

            #call function fron class "Plant" to add plant in shopping cart.
            plant_1.cart()

        # if user choose number 4.
        elif user_input_1 == "4":

            #call function fron class "Plant" to print the recepit.
            plant_1.recepit() 

        # if user choose number 5.
        elif user_input_1 == "5":

            #exit from program
            print("Thank you.\nWe are looking forward to your visit us agian!")
            check == False
            break

            # If the user selects a number or letters other than numbers 1 - 5.
        else:
            raise InvalidInput("Wrong input!! You should enter number from 1 to 5")
        

   
    except InvalidInput as n :
        print(n)





