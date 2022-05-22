def majors_check():
    global user_input_to_get_majors_list
    global std_major
    majors_list = ["Computer Science","Information Systems","Computer Engineering"]
    print("We will show you a list of some university majors, If your specialty is on this list, type YES or NO ")
    for i in majors_list:
        print(f"- {i}.")
    user_input_to_get_majors_list = input("Is it on the list? ")
    user_input_to_get_majors_list.islower()
    if user_input_to_get_majors_list == "yes":
        std_major=input("Type your major:")
        std_major.capitalize()
        if std_major in majors_list:
            return std_major

    elif user_input_to_get_majors_list =="no":
        print("Sorry you can't join")
 
    
try:
    majors_check()
except Exception as ex:
    print(ex)
