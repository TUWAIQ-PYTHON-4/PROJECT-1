
from xml.dom.minidom import Element


def mnue():
    '''
    this method will print mnue to user
    '''
    print(
        "*** WELCOME TO THE BOOK STORE :) ** \n "
        "- Want to add a book ? (Enter 1 plase)  \n "
        "- Want to view all a book in store ? (Enter 2 plase) \n "
        "- Want to find a book? (Enter 3 plase) \n "
        "- Want to find a book price ? (Enter 4 plase) \n "
        "- Want to cheack to the price of the book after discount ? (Enter 5 plase) \n "
        "- Want to Exit ? (Enter 6 plase)"
    )

mnue()



def display_book(dic_book:dict):
    '''
    this method will display all the books in store
    '''
    for key in dic_book.values():
        print(key)
    
def find_book(dic_book:dict,name_book):
    '''
    this method will display info the book the user search
    '''
    if name_book in dic_book.keys():
        if name_book==name_book:
            return dic_book[name_book]
    else:
        return "Sorry, did not find the book"
    
    

def find_price(dic_book:dict,name_book):
    '''
    this method will display price the book the user search
    '''
    #for key in dic_book.keys():
    if name_book in dic_book.keys():
        if name_book==name_book:
            print("Book price is :"+dic_book[name_book][1])
    else:
        print("Sorry, did not find the book")

def discaont_book(price_book):
    '''
    this method cheack if the book Larg than 100 will calclate the price after discount
    '''
    if price_book>100:
        before_discaont= lambda price_book : price_book/100*25
        print("price of the book after discount:")
        print(price_book-before_discaont(price_book))
    else:
        print("Sorry,this book not have discount becouse the price of the book less 100..")








    


