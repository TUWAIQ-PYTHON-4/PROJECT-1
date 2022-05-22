from Project import BagStore # import class
import function # import modulse

# creat dict
bags_dic={"1234":["Tommy","1234","white","550 SAR"]} 
# create object
obj_bags=BagStore("Tommy","1234","white","550 SAR")


input_user=False
# loop
while (not input_user):
    # Error Handling 
    try:
       inp=int(input(""))
       if inp==1:
          number=1
          brand_name=obj_bags.set_nbrandme(input("Enter Brand Name please : "))
          brand_name=obj_bags.get_nbrandme().lower()
          ID_bags=obj_bags.set_ID(input("Enter ID number for Bag please: "))
          ID_bags=obj_bags.get_ID().lower()
          color_bags=obj_bags.set_color(input("Enter the color  please : "))
          color_bags=obj_bags.get_color().lower()
          price_bags=obj_bags.set_price(input("Enter the price please : "))
          price_bags=obj_bags.get_price().lower()
          bags_dic.update({ID_bags:[brand_name,ID_bags,color_bags,price_bags]})
          obj_bags.add_bags()
          function.mnue()
       elif inp==2:
            function.display_bags(bags_dic)
            function.mnue()
       elif inp==3:
            search_bag=input("Enter the ID number please :").lower()
            print(function.find_bags(bags_dic,search_bag))
            function.mnue()
       elif inp==4:
            search_price=input("Enter the ID number pleaseg :").lower()
            function.find_price(bags_dic,search_price)
            function.mnue()
       elif inp==5:
            dis_price=int(input("Enter the price please :"))
            function.discaont(dis_price)
            function.mnue()
       elif inp==6:
            print("THANK YOU FOR VISITING THE BAGS STORE..SEE YOU AGAIN!!")
            input_user=True
            break
       else:
           print("out of options.. please enter number in options")

    except ValueError:
        print("the input is not number, please enter number onlay..")