from Activity import Activity
from Reservation import Reservation

activity_list = []
reservation_list = []

calcPrice = lambda a, b: a * b


# To search for an activity in the list
def search():
    n = input("Enter activity name : ")
    for x in activity_list:
        if n == x.get_name():
            return x


# To count the number of registration in a specific activity
def count_reserv(n):
    count = 0
    for x in reservation_list:
        if n == x.get_activity().get_name():
            count += 1

    return count



print("\tActivities System")

while True:
    try:
        
        
        print("Menu:")
        
        print("1- Add activity")
        print("2- Show activities")
        print("3- View activity info")
        print("4- Reserve activity ")
        print("5- Show reservation list ")
        print("6- Exit")
        userInput = int(input("Choose from the above options : "))

        
        if userInput == 1:

            name = input("Enter activity name : ")
            sd = input("Enter start date : ")
            duration = input("Enter the duration : ")
            place = input("Enter activity place : ")
            capacity = int(input("Enter the capacity : "))
            price = int(input("Enter entry price : "))
            obj = Activity(name, sd, duration, place, capacity, price)
            activity_list.append(obj)
            print("\n** Activity added successfully")

        
        elif userInput == 2:
            if len(activity_list) == 0:
                print("No activities!")
            else:
                for i in activity_list:
                    i.print()

        
        elif userInput == 3:
            if len(activity_list) == 0:
                print("No activities!")
            else:
                o = search()

                if not o:
                    print("Activity not found!")
                else:
                    o.print()

        # Print reserve an activity
        elif userInput == 4:
            if len(activity_list) == 0:
                print("No activities!")
            else:
                o2 = search()

                if not o2:
                    print("Activity not found!")
                else:
                    cnt = count_reserv(o2.get_name())
                    available_tickets = o2.get_capacity() - cnt

                    if available_tickets == 0:
                        print("Sorry, all the ticket reserved!")
                    else:
                        cn = input("Enter your name : ")
                        p = input("Enter your phone number : ")
                        nt = int(input("Enter number of tickets : "))
                        if available_tickets < nt:
                            print("Sorry, there is just \"", available_tickets, "\" tickets")

                        else:
                            obj2 = Reservation(cn, o2, p, nt, calcPrice(nt, o2.get_price()))
                            reservation_list.append(obj2)
                            print("\n**You've successfully booked")
        #To print resrivations
        elif userInput == 5:
            if len(reservation_list) == 0:
                print("No reservations yet!")
            else:
                print("\n")
                print("     Reservation Report       ")
                
                for i in reservation_list:
                    i.print()
                    print()

        #to exit
        elif userInput == 6:
            print("\nThank you for using our program, come back again soon")
            break
        else:
            print('Invalid input!')
    except:
        print('Something went wrong, Please try again !')