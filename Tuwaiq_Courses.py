def Tuwaiq_Courses_Program():
    global user_input_to_get_started
    print("\n -------------------Welcome To Tuwaiq Courses Program------------------\n")
    user_input_to_get_started =  input("Please if you want to start and join the Tuwaiq courses, you must read the terms.\nType YES to read the terms and join or NO to exit :\n")
    print("-----------------------------------------------")
    user_input_to_get_started.islower()
    if user_input_to_get_started == 'yes':
        print("This program requires some conditions")
        print("-----------------------------------------------")
        print("\nTerms of Tuwaiq Courses Program:\n")
        Trems_list= ["You must be Saudi",
                            "You must have a Bachelor's degree or higher in a technical field" , 
                            "Your age should be between 22 to 33",
                            "Not be an employee" ,
                            "You must have a laptop",
                            "Not registered with social insurance"]
        for i in Trems_list:
                print(f"* {i} .\n")
        while True:
                user_input_to_get_agree = input("After you read the terms of the program, do you agree or disagree?")
                user_input_to_get_agree.islower()
                if user_input_to_get_agree == "agree":
                    print("\nTo give you the best service, we would like to verify some information")
                    import majors_user
                    majors_user

                    import Social_Insurance 
                    Social_Insurance

                    import permissible_Age
                    permissible_Age

                
                    from Social_Insurance import user_anser_SI
                    from majors_user import user_input_to_get_majors_list
                    from permissible_Age import user_age
                    if user_anser_SI =="yes" or user_input_to_get_majors_list =="no" or user_age not in range(22,34) :
                        print("Sorry you are not eligible for the Tuwaiq Courses Program")
                        break
                    class Tuwaiq_Std:             
                        def __init__(self , first_name ,last_name, age , major, phone_number, city) :
                                        self.first_name = first_name
                                        self.__last_name = last_name
                                        self.age = age
                                        self.major = major
                                        self.phone_number = phone_number
                                        self.city = city
                                                        
                        def set_fname(self,first_name):
                            self.first_name = first_name

                        def get_fname(self):
                            return self.first_name

                        def set_lname(self,last_name):
                            self.__last_name = last_name

                        def get_lname(self):
                            return self.__last_name

                        def std_check_info():
                            while True:
                                stud_list=[] 
                                first_name =input("First Name:").title()
                                last_name = input("Last Name:").title()
                                from permissible_Age import user_age
                                age = user_age
                                from majors_check import std_major
                                major =std_major
                                phone_number = input("Phone Number:")
                                if len(phone_number)>10:
                                    raise print("The number entered is incorrect, check the number again")
                                city = input("Your City:").title()
                                print("---------------------------------------------")
                                stud_list.append(first_name)
                                stud_list.append(last_name)
                                stud_list.append(age)
                                stud_list.append(major)
                                stud_list.append(phone_number)
                                stud_list.append(city)
                                std=Tuwaiq_Std(first_name , last_name,user_age,major,phone_number,city)
                                full_name = lambda first, last: f' {first.title()} {last.title()}'
                                                                
                                print(f"{full_name(std.get_fname(),std.get_lname())} information :",stud_list)
                                std_sure=input("Are you sure that your information is correct? yes or no :")
                                std_sure.islower()
                                if std_sure == "yes":
                                    print("---------------------------------------------")
                                    print("\n Thank you for your registration, we look forward to accepting you soon \n Regards:\n Tuwaiq Team")
                                    break
                                elif std_sure =="no":
                                    print("Try agine")
                                            

                    class Courses:
                        def __init__(self,course_name ,course_time, course_teacher) :
                                        self.course_name = course_name 
                                        self.course_time = course_time
                                        self.course_teacher = course_teacher

                        def courses_show():
                            print("You are eligible for the Tuwaiq Courses Program")
                            course_show=input("- Would you like to check out the available courses? -\n")
                            print("------------------------------------")
                            if course_show =="yes":
                                python=Courses("Python","5-9 PM" ," Mr.Aqeel")
                                java=Courses("Java","5-9 PM","The teacher has not yet been appointed")
                                print(f"First Course: {python.course_name} | Time:{python.course_time} | Teacher:{python.course_teacher}\n")
                                print(f"Second Course:: {java.course_name} | Time:{java.course_time} | Teacher:{java.course_teacher}")
                                print("------------------------------------")
                                join_class.check_join_class()
                            elif course_show == 'no':
                                print("Thank you for you time ")
                        
                    class join_class(Courses):
                        def check_join_class():
                            while True:
                                print("Which Course Do You Want To Join , If you do not want to join the courses, type EXIT ")
                                std_course_want=input("1.Python or 2.Java -\n just type course number :")
                                std_course_want.islower()
                                if std_course_want == '1':
                                    print("\nYou must fill out the form to register in Python Course")
                                    print("---------------------------------------------")
                                    Tuwaiq_Std.std_check_info()
                                    break
                                elif std_course_want == '2':
                                    print("You must fill out the form to register in Java Course")
                                    Tuwaiq_Std.std_check_info()
                                    break
                                elif std_course_want == "exit":
                                    print("Thank you, we hope to see you later \nRegards:\nTuwaiq Team")
                                    break
                    Courses.courses_show()
                    break
                elif user_input_to_get_agree == "disagree":
                    print("Thank you , We wish you good luck")
                    print("------------------------------TUWAIQ TEAM------------------------------")
                    break
    elif user_input_to_get_started == "no":
        print("Thank you , We wish you good luck ")
    
print("------------------------------TUWAIQ TEAM------------------------------")
                
            
            



Tuwaiq_Courses_Program()