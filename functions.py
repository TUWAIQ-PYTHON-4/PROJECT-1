from books import *

class WrongInput(Exception):
    ''' raised only if wrong input from user '''

def user_option_input(answer):
    '''This function raise error if user enters wrong input'''

    input_option=['1', '2', '3', '4']
    if answer not in input_option:
        raise WrongInput('Sorry, wrong input please enter a number from the given options.')
    

def view_books_info(user_option):
    ''' This function views used book information choosen by user'''

    if user_option == '1':
        print(f'Book Title: {book1.get_name()}\n',
        f'Genre: {book1.get_genre()}\n',
        f'Summary: {book1.get__summuray()}\n',
        f'Rating: {book1.get__rating()}\n',
        f'Book Condition: {book1.get__condition()}\n',
        f'Price: {book1.get_price()}\n')

    elif user_option == '2':
        print(f'Book Title: {book2.get_name()}\n',
        f'Genre: {book2.get_genre()}\n',
        f'Summary: {book2.get__summuray()}\n',
        f'Rating: {book2.get__rating()}\n',
        f'Book Condition: {book2.get__condition()}\n',
        f'Price: {book2.get_price()}\n')
        

    elif user_option == '3':
        print(f'Book Title: {book3.get_name()}\n',
        f'Genre: {book3.get_genre()}\n',
        f'Summary: {book3.get__summuray()}\n',
        f'Rating: {book3.get__rating()}\n',
        f'Book Condition: {book3.get__condition()}\n',
        f'Price: {book3.get_price()}\n')

def add_book_to_cart(user_cart, user_orders_total,user_option):
    ''' This function adds books choosen by users to their shopping cart'''

    if user_option == '1':
        if book1.get_name() not in user_cart:
            user_cart.append(book1.get_name())
            user_orders_total.append(book1.get_price())
        else:
            print('Book already added to your cart')

    elif user_option == '2':
        if book2.get_name() not in user_cart:
            user_cart.append(book2.get_name())
            user_orders_total.append(book2.get_price())
        else:
            print('Book already added to your cart')
        

    elif user_option == '3':
        if book3.get_name() not in user_cart:
              user_cart.append(book3.get_name())
              user_orders_total.append(book3.get_price())
        else:
            print('Book already added to your cart')

