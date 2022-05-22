def Social_insurance(): 
    global user_anser_SI
    while True:
        user_anser_SI = input("Are you registered with social insurance ?")
        user_anser_SI.islower()

        if user_anser_SI =="yes":
            
            break
        elif user_anser_SI == "no":
            print("")
            break
        else:
            print("Sorry, your answer is not clear , Try again")
            
try:            
    Social_insurance()
except Exception as er:
    print(er)

