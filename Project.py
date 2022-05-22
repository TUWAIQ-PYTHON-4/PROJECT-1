# create class
class BagStore:
     def __init__(self,brand, ID, color, price):
        #instance properties / Attribues
        self.__brand = brand
        self.__ID= ID
        self.__color = color
        self.__price=price

# set and get 
     def set_nbrandme(self, brand):
        self.__brand = brand
     def get_nbrandme(self):
        return self.__brand
     def set_ID(self, ID):
        self.__ID = ID
     def get_ID(self):
        return self.__ID
     def set_color(self, color):
        self.__color = color
     def get_color(self):
        return self.__color
     def set_price(self, price):
        self.__price =price 
     def get_price(self):
        return self.__price

     def add_bags(self):
        '''function for display bags informations the user'''
        print ("bag informations : \n " 
        "Brand name of the bag:"+ self.get_nbrandme()+" \n "
        "ID number of the Bag:"+ self.get_ID()+" \n "
        "color of the bag:"+ self.get_color()+" \n "
        "price bag:"+ self.get_price()+" \n ")