
from sre_compile import isstring


class LibraryBook:#Use at least 1 Class.

    def __init__(self) -> None:
        #Use lists or dictionaries or tuples.
       self.book=['Dune','Harry potter','1984','Gone','Fallen','Echo','Twilight','xo','poison']

    def search_(self):
        user_input1=input('Please Enter Name of book you want ')
        try:#Use some form of Error Handling .
            user_input1 != isstring()
        except TypeError as te:
            print("")  
        while True:
            if user_input1 in self.book:
                print('Here is your book : ',user_input1)
                break
            elif user_input1 not in self.book:
                print('Sorry the book you want is not Avaible !')
                break
            raise TypeError ("Sorry invalid value !!")
            
    def add_(self):#Use functions that return an output .
        user_input2=input('Please write Name of Book you want add :')
        self.book.append(user_input2)
        return print('Thank you your book has added to the Library ') 
    
    def dislay_book(self):
         display_book = list(map(lambda x: x, self.book))#Use a Lambda function.
         print(display_book)
         print('The number of book in my library is : ',len(self.book)) 