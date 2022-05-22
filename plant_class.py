from functools import reduce

#this is counter for number of add in shopping cart.
add_cart=0
#create class.
class Plant():
    
    #instance properties
    def __init__(self):
        self.__name = ["Fix Decora","boots","cycas palm","Marie Gold","Silosia","Camelia Dutch","Spathiphyllum"] #private
        self.__type = ["indoor","indoor","outdooor","outdoor","outdoor","indoor","indoor"] #private
        self.__length = [45,100,40,20,30,25,20] #private
        self.__price = [175,5,350,2,170,35,75] #private
        self.__shopping_cart = [[0 for j in range(4)] for i in range(add_cart)] #private  
        self.__cost = []#private
        self.__buy_plant_name = []#private


    #creating a setter and getter function 
    def set_name(self,name):
        self.__name = [name]

    def get_name(self):
        return self.__name

    def set_type(self,type):
        self.__type = [type]

    def get_type(self):
        return self.__type

    def set_length(self,length):
        self.__length = [length]
    
    def get_length(self):
        return self.__length

    def set_price(self,price):
        self.__price = [price]

    def get_price(self):
        return self.__price

    def set_shopping_cart(self,shopping_cart):
            self.__shopping_cart = shopping_cart
      
    def get_shopping_cart(self):
        return self.__shopping_cart[:][:]

    def set_cost(self,cost):
        self.__cost = cost

    def get_cost(self):
        return self.__cost
    
    def set_buy_plant_name(self,buy_plant_name):
        self.__buy_plant_name = buy_plant_name

    def get_buy_plant_name(self):
        return self.__buy_plant_name

    #create function to print information of plants.
    def info_plants(self):

        i =0
        cont = len(self.__name)
        print("________________________________")
        print("      PLANTS INFORMATION        ")
        print("________________________________")

        #check if there is any plants in store.
        if cont > 0:

            #if store has at least plane then print all information about it.
            while cont != 0:
                print("")
                print(f"      PLANT {i+1}         ")
                print(f"Plant Name: {self.get_name()[i]}\nPlant Type: {self.get_type()[i]} plant\nPlant Length: {self.get_length()[i]} cm\nPlant Price: {self.get_price()[i]} SAR")
                i +=1
                cont -=1
        #if no plant in store then print this.
        else:
            print("There are no Items!!")


    #create function to add in shopping cart.
    def cart(self):
        
        #check if there is any plants in store.
        while len(self.__name) > 0:

            #make the "add_cart"counter global and increase the counter by one.
            global add_cart
         

            print("Choose number of plant you want to buy it: ")
            print("________________________________")
            print("          PLANTS NAMES          ")
            print("________________________________")

            #this for loop to display all plants in store.
            cont = 1
            for plant in self.get_name():
                print(f"      {cont}: {plant}")
                cont +=1
            print("________________________________")

            #take the user input and check if it in the list . if yes we will add it in shopping.
            plant_number = input() 
            
            if int(plant_number) == 1 or int(plant_number) == 2 or int(plant_number) == 3 or int(plant_number) == 4 or int(plant_number) == 5 or int(plant_number) == 6 or int(plant_number) == 7 :
                self.set_shopping_cart=self.__shopping_cart.insert(add_cart,[self.get_name()[int(plant_number)-1],self.get_type()[int(plant_number)-1],self.get_length()[int(plant_number)-1],self.get_price()[int(plant_number)-1]])
                print("       Added successfully!!   ")
                add_cart +=1
                break

            #if user input not in list so print this.
            else:
                print("There are no Items whit is number!!")


    #create function to print the recepit.
    def recepit(self):
    
        print("--------------------------------")
        print("--------------------------------")
        print("            RECEPIT             ")
        print("--------------------------------")
        print("--------------------------------")
        
        #check if there is any item in shopping cart,if yes do this. 
        if add_cart != 0:
           
            #if it has item in shopping cart do this.
            #add all value of price in a new list call it "cost"
            self.set_cost = self.__cost.append(self.get_shopping_cart()[add_cart-1][3])
            self.set_buy_plant_name = self.__buy_plant_name.append(self.get_shopping_cart()[add_cart-1][0])
            
            listSum = reduce(lambda a,b:a+b,self.get_cost())
            for i in range(add_cart):
                print(f"{self.get_buy_plant_name()[i]}       SAR {self.get_cost()[i]}")
            print("\n--------------------------------")
            print(f"TOTAL AMOUNT             SAR {listSum}")
            print("--------------------------------")
        ##check if there is any item in shopping cart, if no do this. 
        else:
            print("There are no Items in your shopping cart!!")


        

            

    

    