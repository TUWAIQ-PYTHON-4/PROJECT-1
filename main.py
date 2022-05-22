
from books import *
from functions import *


# for adding books chose by user
shopping_cart= []

# To sum the user total order
total_order= []

# to filter the best seller books which ratings are above 4
books_rating= {book1.get_name(): book1.get__rating(), book2.get_name(): book2.get__rating(), book3.get_name(): book3.get__rating()}
best_seller= dict(filter(lambda rating: rating[1] > 4, books_rating.items()))

while True:

    print('Welcome to Second Hand BookStore')
    print(  '1 - View second hand Books\n',
            '2 - View the bestseller Second hand Books\n',
            '3 - View cart\n',
            '4 - Checkout\n')
    
    user_input = input('choose by number from the options above: ')

    # Handling input error the user should only type from numbers 1 to 4
    try:
        user_option_input(user_input)

    except WrongInput as w:
        print(w,'\n')
    

     # view the books and add from them by book number
    if user_input == '1':

        print(f'1 - {book1.get_name()}\n',f'2- {book2.get_name()}\n',f'3- {book3.get_name()}\n') 

        user_books_view= input('would you like to view Book information? type in book number: ')
        view_books_info(user_books_view)

        user_add_book= input('Do want to add a book to your cart? add by book number: ')
        add_book_to_cart(shopping_cart, total_order,user_add_book)

     # view the books which are bestsellers and add from them by book number
    elif user_input == '2':

        print('Bestseller books with a rating above 4 stars: ','\n')

        for key, value in best_seller.items():
             print('-',key,'\n')

        user_add_book= input('Do want to add a book from bestsellers to your cart? add by book number: ')
        add_book_to_cart(shopping_cart, total_order,user_add_book)
     
     # view user shopping cart
    elif user_input == '3':
        print('Your Shopping Cart:','\n')
        for book in shopping_cart:
            print('-',book,'\n')
        
      # view user total order           
    elif user_input == '4':

        total=sum(total_order)

        if total == 0:
            print('Thank you for stopping by please visit again')
        else:
            print(f"Thank you. Here is your orders total: {total}")
        break




