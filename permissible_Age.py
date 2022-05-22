def permissible_Age():
    global user_age
    
    while True:
        user_age =int( input("please Enter age :"))
        if len(str(user_age)) >2:
            print("The entry is incorrect, make sure the answer must be only two digits")
            
        elif user_age in range(22 , 34):
            print("")
            return user_age
            
        else:
            print("Sorry you can't join")
            break
    
try:
    permissible_Age()
except Exception as er:
    print(er)

