menu_item = {'1' : 'Coupcake', '2': 'TeaCake',\
             '3' : 'Dounts', '4' : 'Coffe',\
             '5' : 'MilkShake', '6' : 'Water'}


class Customer:
    '''
    this class contane the
    '''

    def __init__(self, orders: dict = { }) -> None:
        self.__order = orders

    def _set_orders_(self, item: tuple, quantity: int) -> None:
        '''
        this method takes a tuple (item number in menu, cost per one unit) and an intger
        that represent the quintity desiered to be bought. the first elemint in the tuple is used to create the key.
        the second elemint in the tuple with the quintity are asignd as value to the key.
        '''
        self.__order[item[0]] = (item[1]*int(quantity),quantity)


    
    def get_order(self)-> dict:
        '''
        return the object order
        '''
        return self.__order



    def _inquiry(self) -> bool:
        '''
        print out the object order
        '''
        temp = self.get_order()
        if temp:
         for key,val in temp.items():
          print(f'\033[35;1m{menu_item[key]} x{val[1]}...{val[0]}')
        else: 
            print('Empty shopping chart...')
            return False
        return True

    def _calc_total_(self)-> int:
        '''
        this method calculate the total of the items in the shopping cart.
        '''
        temp = list(map( lambda c : c[0] ,list(self.get_order().values())))
        return sum(temp)


    def _delete_item(self, key: str) -> bool:
        '''
        delet an elemint from the order dictionary
        '''
        if self.__order :
         try:
          temp = list(menu_item.values()).index(key.title())
          del self.__order[str(temp+1)]
         except Exception as e:
            print('\nNo such item exist in your shopping cart...')
            return False
         else:
             print('\nThe item has been deleted')
             return True

    
        