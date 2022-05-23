from unicodedata import name
from Project_1 import *

class Delivery:

    def __init__(self, name:str, address, phone:int):
        self.__name = name 
        self.__address = address
        self.__phone = phone
    
    
    
    def set__name(self,name:str):
        self.__name = name
    def get_nabrandme(self):
        return self.__name
    
    def set__address(self,address):
        self.__address = address
    def get_address(self):
        return self.__address
    def set__phone(self,phone:int):
        self.__phone = phone
    def get_phone(self):
        return self.__phone






    __name=input("Enter your name:")
    a=__phone=input("Enter your phone:")
    __address=input("Enter your address:")
    print("Your name",__name,"& your phone",__phone,"& your address",__address )
    
   
   



   