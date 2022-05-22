import random
import brands

class LaptopFinder:
    def start():
        print('''\nWelcome to Laptop Finder Application ** Find The Laptop That Suits Your Needs **
        - To Show All Products:                                       [Enter "1"]
        - To Show Product Based On Types:                             [Enter "2"]
        - To Search For Brand:                                        [Enter "3"]
        - To Show Product Based On Price and Brand:                   [Enter "4"]
        - To Get Some Recommendations:                                [Enter "5"]   
        - Make it fun and Choose Randomly                             [Enter "6"]
        - To List The best Market/Store That sell Your Favorite Brand [Enter "7"]
        - To Exit the program:                                        [Enter "0"]
        ''')
        global opertion
        opertion = int(input('Type in Your Operation: '))

    def show_all():
        # print all hp laptop types
        for type, type_info in brands.hp.items():
            print("\nBrand: Hp\nType:", type)  
            for key in type_info:
                print(key + ':', type_info[key])

        for type, type_info in brands.apple.items():
            print("\nBrand: Apple\nType:", type)  
            for key in type_info:
                print(key + ':', type_info[key])

        for type, type_info in brands.lenovo.items():
            print("\nBrand: Lenovo\nType:", type)  
            for key in type_info:
                print(key + ':', type_info[key])

        for type, type_info in brands.dell.items():
            print("\nBrand: Dell\nType:", type)  
            for key in type_info:
                print(key + ':', type_info[key])
    
    def search(option: int):
        if option == 1:
            for type, type_info in brands.hp.items():
                print("\nType:", type)  
                for key in type_info:
                    print(key + ':', type_info[key])
        elif option == 2:
            for type, type_info in brands.apple.items():
                print("\nType: ", type)  
                for key in type_info:
                    print(key + ':', type_info[key])

        elif option == 3:
            for type, type_info in brands.lenovo.items():
                print("\nType: ", type)  
                for key in type_info:
                    print(key + ':', type_info[key])       

        elif option == 4:
            for type, type_info in brands.dell.items():
                print("\nType: ", type)  
                for key in type_info:
                    print(key + ':', type_info[key])
            
    def list_type_based():
        print('\nSearch Based on your Purpose: \n 1- Power User \n 2- Everyday use \n 3- Creative Professional \n 4- Business \n 5- Gaming')
        option = int(input('Type in the number please: '))
        if option == 1:
            print('Brand : HP \n',brands.hp['Power User'],'\n')
            print('Brand : Apple \n',brands.apple['Power User'],'\n')
            print('Brand : lenovo \n',brands.lenovo['Power User'],'\n')
            print('Brand : Dell \n',brands.dell['Power User'],'\n')
        elif option == 2:
            print('Brand : HP \n',brands.hp['Everyday use'],'\n')
            print('Brand : Apple \n',brands.apple['Everyday use'],'\n')
            print('Brand : lenovo \n',brands.lenovo['Everyday use'],'\n')
            print('Brand : Dell \n',brands.dell['Everyday use'],'\n')
        elif option == 3:
            print('Brand : HP \n',brands.hp['Creative professional'],'\n')
            print('Brand : Apple \n',brands.apple['Creative professional'],'\n')
            print('Brand : lenovo \n',brands.lenovo['Creative professional'],'\n')
            print('Brand : Dell \n',brands.dell['Creative professional'],'\n')
        elif option == 4:
            print('Brand : HP \n',brands.hp['Business'],'\n')
            print('Brand : Apple \n',brands.apple['Business'],'\n')
            print('Brand : lenovo \n',brands.lenovo['Business'],'\n')
            print('Brand : Dell \n',brands.dell['Business'],'\n')
        elif option == 5:
            print('Brand : HP \n',brands.hp['Gaming'],'\n')
            print('Brand : Apple \n',brands.apple['Gaming'],'\n')
            print('Brand : lenovo \n',brands.lenovo['Gaming'],'\n')
            print('Brand : Dell \n',brands.dell['Gaming'],'\n')
        else:
            print('Please enter one of the above numbers ')

    def recomendations(brand, type):
        if brand == 1 :
            if type == 1 :
                print('\nI suggest for you\n',brands.hp['Power User'],'\n')
            elif type == 2 :
                print('\nI suggest for you\n',brands.hp['Everyday use'],'\n')
            elif type == 3 :
                print('\nI suggest for you\n',brands.hp['Creative professional'],'\n')
            elif type == 4 :
                print('\nI suggest for you\n',brands.hp['Business'],'\n')
            elif type == 5 :
                print('\nI suggest for you\n',brands.hp['Gaming'],'\n')

        elif brand == 2 :
            if type == 1 :
                print('\nI suggest for you\n',brands.apple['Power User'],'\n')
            elif type == 2 :
                print('\nI suggest for you\n',brands.apple['Everyday use'],'\n')
            elif type == 3 :
                print('\nI suggest for you\n',brands.apple['Creative professional'],'\n')
            elif type == 4 :
                print('\nI suggest for you\n',brands.apple['Business'],'\n')
            elif type == 5 :
                print('\nI suggest for you\n',brands.apple['Gaming'],'\n')

        elif brand == 3 :
            if type == 1 :
                print('\nI suggest for you\n',brands.lenovo['Power User'],'\n')
            elif type == 2 :
                print('\nI suggest for you\n',brands.lenovo['Everyday use'],'\n')
            elif type == 3 :
                print('\nI suggest for you\n',brands.lenovo['Creative professional'],'\n')
            elif type == 4 :
                print('\nI suggest for you\n',brands.lenovo['Business'],'\n')
            elif type == 5 :
                print('\nI suggest for you\n',brands.lenovo['Gaming'],'\n')

        elif brand == 4 :
            if type == 1 :
                print('\nI suggest for you\n',brands.dell['Power User'],'\n')
            elif type == 2 :
                print('\nI suggest for you\n',brands.dell['Everyday use'],'\n')
            elif type == 3 :
                print('\nI suggest for you\n',brands.dell['Creative professional'],'\n')
            elif type == 4 :
                print('\nI suggest for you\n',brands.dell['Business'],'\n')
            elif type == 5 :
                print('\nI suggest for you\n',brands.dell['Gaming'],'\n')  
                
    def specfication(brand:int, price: int):
        if brand == 1 :
            values:list = list(map( lambda key: brands.hp[key] if brands.hp[key]['price'] >= price else '', brands.hp.keys()))
            for x in values:
                print(x) 

        elif brand == 2:
            values:list = list(map( lambda key: brands.apple[key] if brands.apple[key]['price'] >= price else '', brands.apple.keys()))
            for x in values:
                print(x)  

        elif brand== 3:
            values:list = list(map( lambda key: brands.lenovo[key] if brands.lenovo[key]['price'] >= price else '', brands.lenovo.keys()))
            for x in values:
                print(x) 

        elif brand == 4:
            values:list = list(map( lambda key: brands.dell[key] if brands.dell[key]['price'] >= price else '', brands.dell.keys()))
            for x in values:
                print(x) 
 
    def random_hp() -> list:
        return random.choice(list(brands.hp.items())) 

    def random_dell() -> list:
        return random.choice(list(brands.dell.items()))

    def random_apple() -> list:
        return random.choice(list(brands.apple.items()))
   
    def random_lenovo() -> list:
        return random.choice(list(brands.lenovo.items()))  
    
    def best_market() ->list:
        print(''' 
        - To List the Best Market/Store that sell your Labtop based on brand:
        1- Hp
        2- Apple
        3- Lenovo
        4- Dell
        ''')
        select = int(input('Type in the number: '))
        if select == 1:
            return brands.hp_market
        elif select == 2:
            return brands.apple_market
        elif select == 3:
            return brands.lenovo_market
        elif select == 4 :
            return brands.dell_market

# From here the program starts

lab = LaptopFinder
try:
    while True:
        lab.start()

        if opertion == 0:
            print("Exiting the Program \nThank you for using Laptop Finder Application, come back again soon")
            exit()

        elif opertion == 1:
            lab.show_all()

        elif opertion == 2:
            lab.list_type_based()

        elif opertion == 3:       
            select=int(input('\nWe have: \n1- Hp \n2- Apple \n3- Lenovo \n4- Dell \nType in the number: '))
            lab.search(select)

        elif opertion == 4:
            brand_selection = int(input('\nChoose Your Favorite Brand , We have: \n1- Hp \n2- Apple \n3- Lenovo \n4- Dell \nType in the number: '))
            price_selection = int(input('\nSet The Budget Range: '))
            print()
            lab.specfication(brand_selection,price_selection)

        elif opertion == 5:
            print('\nI am here to filter your options: ')
            brand_selection = int(input('\nChoose Your Favorite Brand , We have: \n1- Hp \n2- Apple \n3- Lenovo \n4- Dell \nType in the number: '))
            print('\nWhat is your purpose? choose one of the below: ')
            type_selection = int(input(' 1- Power User \n 2- Everyday use \n 3- Creative professional \n 4- Business \n 5- Gaming \nType in the number: '))
            lab.recomendations(brand_selection,type_selection)

        elif opertion == 6:
            random_all = [lab.random_hp, lab.random_dell , lab.random_apple , lab.random_lenovo]
            print(random.choice(random_all)())
        
        elif opertion == 7:
            print(lab.best_market())
            
        else:
            print('Please enter one of the above numbers ')

except ValueError as e:
    print(e)
except Exception as e:
    print(e)



