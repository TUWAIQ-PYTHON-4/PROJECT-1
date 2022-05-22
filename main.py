import shutil
from Customers import Customer

menu_item_pricess =  { '1' : 18.50, '2': 15.00,\
               '3' : 5.00, '4' : 9.00,\
               '5' : 4.00, '6' : 1.00 }

def print_menu():
   col = shutil.get_terminal_size().columns
   print('\033[35;1m -----------------------COFFEE SHOP MENU-----------------------\n'.center(col))
   file = open('PROJECT-1/menu_item.txt', 'r').read()
   menu = "\n".join(line.center(col)  for line in file.split("\n"))
   print(f'\033[37;1m{menu}')

print_menu()




while True:
 customer = Customer()
 answer = input('\n\033[37;1mEnter\t1 to see your shopping cart\n\t2 to add items into the shopping cart\n\t3 to delete from shoping cart\n\t4 to view the menu\n\tand 0 to check out : ')
 match answer:
    case '1':
     customer._inquiry()

    case '2':
      try:
       item = input('Enter the item number as it shown in the menue : ')
       assert isinstance(int(item), int) and  menu_item_pricess[item]
       quantity = input('Enter the amount you want to add from the item : ')
       # method to enter the item into the order dict in object of type Customer
       customer._set_orders_( (item,menu_item_pricess .get(item)), int(quantity))
      except Exception as e:
          print('Please enter one of the numbers on the menue...')

    case '3':
        if customer._inquiry():
         item_to_delete = input('Enter the name of the item you want to delete : ').replace(' ','').lower()
         customer._delete_item(item_to_delete)

    case '4':
        print_menu()

    case '0':
        # print orders with amount if exisit and tell taht it well be delevered within 30 min and pay cash only
         print('\nThank you and come againe')
         print('you ordered : ')
         customer._inquiry()
         print(f'Total cost .... {customer._calc_total_()}')
         print('\033[31;1mPrepare you mony we only accept cash...')
         break

    case _:
        print('\nEnter 1, 2, 3, 4, or 0 only')

    

