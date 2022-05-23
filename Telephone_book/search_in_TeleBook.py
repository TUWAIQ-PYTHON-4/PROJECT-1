import entering_number as en
 
en.telephone_book


def search_in_telebook():

    

  search = input("Enter the number you are looking for: ")


  if search in en.telephone_book:
       print(en.telephone_book[search])

  elif len(search) < 10 or len(search) > 10 or not (search.isdigit()):
    print("This is invalid number")  

  elif search not in en.list:
    print("Sorry, the number is not found")

search_in_telebook()