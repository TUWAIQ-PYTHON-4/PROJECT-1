
majors_list = ["Computer Science","Information Systems","Computer Engineering"]
print("We will show you a list of some university majors, If your specialty is on this list, type YES or NO\n ")
for i in majors_list:
    print("\n"f"- {i}.")

def majors_user_():
    global user_input_to_get_majors_list
    user_input_to_get_majors_list = input("\nIs it on the list? ")
    user_input_to_get_majors_list.islower()
    if user_input_to_get_majors_list == "yes":
        print("")
        return user_input_to_get_majors_list
        
    elif user_input_to_get_majors_list =="no":
        
        return user_input_to_get_majors_list
    
try:
    majors_user_()
except Exception as ex:
    print(ex)

