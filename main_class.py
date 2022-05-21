from class_book import Book
import methods 


book_dic={"HTML":["Introduction in HTML","30 SAR","2018","Noura"]}
#book_dic={}
obj_book=Book("Html","30 SAR","2018","Noura")


input_user=False
while (not input_user):
    try:
       ask=int(input(""))
       if ask==1:
          number=1
          name_book=obj_book.set_name(input("Enter please name book : "))
          name_book=obj_book.get_name().lower()
          price_book=obj_book.set_price(input("Enter please price book : "))
          price_book=obj_book.get_price().lower()
          year_book=obj_book.set_year(input("Enter please the book year : "))
          year_book=obj_book.get_year().lower()
          outhor_book=obj_book.set_outhor(input("Enter please author book : "))
          outhor_book=obj_book.get_outhor().lower()
          book_dic.update({name_book:[name_book,price_book,year_book,outhor_book]})
          obj_book.add_book()
          #print(book_dic)
          methods.mnue()
       elif ask==2:
            methods.display_book(book_dic)
            methods.mnue()
       elif ask==3:
            search_book=input("Enter please the name of the book :").lower()
            print(methods.find_book(book_dic,search_book))
            methods.mnue()
       elif ask==4:
            search_price=input("Enter please the name of the book :").lower()
            methods.find_price(book_dic,search_price)
            methods.mnue()
       elif ask==5:
            dis_price=int(input("Enter please the price of the book :"))
            methods.discaont_book(dis_price)
            methods.mnue()
       elif ask==6:
            print("THANK YOU FOR VISITING THE BOOK STORE..BEY BEY :)")
            input_user=True
            break
    except:
        print("THIS IS NOT NUMBER..PLEASE ENTER NUMBERS ONLY..")
    
    
    
