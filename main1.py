from library_book1 import *
class main(LibraryBook): 
#Must be interactive on CLI.
 input_user=input('Hello ! you are at Nan Library : \n if you want to search a specific book enter search \n if you want to add a book enter add \n if you want to display all book enter display\n if you want to exit prgramm enter exit ')
 l2=LibraryBook()
 while True :#Use loops.
    if input_user=='exit': 
        print('Thank you !')
        break
    elif input_user=='search': 
        l2.search_() 
        break
    elif input_user=='add':
        l2.add_()
        l2.dislay_book()
        break
    elif input_user == 'display':
        l2.dislay_book()
        break
