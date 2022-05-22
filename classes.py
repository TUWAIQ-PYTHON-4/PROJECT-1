from colorama import Fore
class InvalidInput(Exception):
    '''raised only if wrong input from user'''
class products:
    def __init__(self):
        self.__brand = ["Apple"]
        self.__name = ["Iphone 13","Iphone 13 pro","Iphone 13 pro max","Ipad pro","AirPods pro"]
        self.__price = [4000,5000,5300,4800,999]
        self.__size = ["256Gb","256Gb","256Gb","256Gb",""]
        self.__quantity = [3,3,5,2,5]
    
    def set_brand(self, brand):
        if isinstance(brand, str):
            self.__brand = [brand]
    def get_brand(self):
        return self.__brand
    def set_name(self, name):
            self.__name = [name]
    def get_name(self):
        return self.__name
    def set_price(self, price):
            self.__price = [price]
    def get_price(self):
        return self.__price
    def set_size(self, size):
            self.__size = [size]
    def get_size(self):
        return self.__size
    def set_quantity(self, quantity):
            self.__quantity = [quantity]
    def get_quantity(self):
        return self.__quantity
    def info_products(self):
        i =0
        count = len(self.__name)
        print("\n     ******    PRODUCTS    ******     ")
        while count != 0:
            print("")
            print(f"               PRODUCT {i+1}         ")
            print(f"         Product Name: {self.get_name()[i]}\n         Product Price: {self.get_price()[i]} SAR\n         Product Size: {self.get_size()[i]}")
            i +=1
            count -=1
#def errors():
#    if answer