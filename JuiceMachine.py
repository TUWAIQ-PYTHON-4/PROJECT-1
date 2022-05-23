import os
class Juice:
    

    def __init__(self, fruit, cups, water, ice):
        self.fruit = fruit
        self.cups = cups
        self.water = water
        self.ice = ice

    def juice_maker(self):
        preferred_juice = type_of_juice()
        ice_intake = some_ice()
        
                

        if preferred_juice == 1:
            print("Orange juice coming up!\n")
            print("1 Orange juice delivered!")
            

        elif preferred_juice == 2:
            print("Apple juice coming up!\n")
            print("1 Apple juice delivered!")

        elif preferred_juice == 3:
            print("Lemon juice coming up!\n")
            print("1 Lemon juice delivered!")
            

        elif preferred_juice == 4:
            print("Grape juice coming up!\n")
            print("1 Grape juice delivered!")
        self.fruit -=140
        self.cups -= 1
        self.ice -= 80
        self.water-= 150
            

    
    def juice_maker_report(self):  
        return {"Fruit": self.fruit, "Water": self.water, "ice": self.ice, "Cups": self.cups}


def type_of_juice():  
    # input
    print("Hi there, what would you like to drink")
    juice_list = ["1 - Orange juice", "2 - Apple juice", "3 - Lemon juice", "4 - Grape juice"]

    valid = False
    while not valid:
        try:
            choice = int(input("Enter Choice: "))
            if choice in (1, 2, 3, 4):
                valid = True
            else:
                print("Please enter a valid option.")
        except ValueError:
            print("Please enter a valid option")

    return choice
def some_ice():

    valid = False

    while not valid:
        try:
            choice = input("Some Ice? ")
            if choice in ("Y", "y", "N", "n"):
                valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")

    return choice


def main():
    os.system("cls")
    new_juice = Juice(3000,25,2000,1000)  # gm, no., ml, gm, 
    print(new_juice.juice_maker_report())
    new_juice.juice_maker()
    print(new_juice.juice_maker_report())


if __name__ == '__main__':
    main()
        