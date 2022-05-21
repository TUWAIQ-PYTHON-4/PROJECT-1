class Book:
    def __init__(self,name,price,year,outhor):
        self.__name=name
        self.__price=price
        self.__year=year
        self.__outhor=outhor
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name

    def set_price(self,price):
        self.__price=price
    def get_price(self):
        return self.__price

    def set_year(self,year):
        self.__year=year
    def get_year(self):
        return self.__year

    def set_outhor(self,outhor):
        self.__outhor=outhor
    def get_outhor(self):
        return self.__outhor
    
    def add_book(self):
        '''
        this method will display info the books the user
        '''
        print ("- Added book info : \n " 
        "name of the book:"+ self.get_name()+" \n "
        "price of the book:"+ self.get_price()+" \n "
        "year of the book:"+ self.get_year()+" \n "
        "outhor of the book:"+ self.get_outhor()+" \n "
         )
    
#Book1=Book("n","n","n","n")
#print(Book1.get_name())













    
    
