

import exception as ex

print('Welcome to the Telephone Book program \n')

def telephone_book():
    

    while True:

        ask_user = input("Do you want to add a new number? ")

        if ask_user == "yes":

          
          input_num = input("Enter the numder: ")
          input_f_name = input("Enter the first name: ")
          input_l_name = input("Enter the last name: ")
          input_email = input("Enter the email: ")
          input_address = input("Enter the address: ")


          list = [input_num,input_f_name,input_l_name,input_email,input_address]

          print(" - ".join(list))

          file = open("Telehpone_Book.txt", "a", encoding="utf-8")


          file.write("Number: " + input_num + "\n" + "Ferst Name: " + input_f_name + "\n" + "Last Name: " + input_l_name + "\n"+ 
          "Email: " + input_email + "\n"+ "Address: "+input_address+ "\n" + "-"*100 + "\n")


          del list


        elif ask_user == "no" :
            break

    

telephone_book()


