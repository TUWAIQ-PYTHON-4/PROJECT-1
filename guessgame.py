# guessing game
from random import randint

def guessing_game():
    user_input = input("Enter the number of the level that you want: \n [1] for Hard level \n [2] for Medium level \n [3] for Easy level \n")
    print('The number is between 1 and 20')
    if user_input == '1' :
        print('You have 6 chances')
        rand_num = randint(1, 20) # function for choose random number
        for i in range(0,6):
            guess_num = int(input('Guess a number ? '))
            if guess_num == rand_num : # check if the number equal or less or bigger
                print("Great !! guess right")
            elif guess_num < rand_num :
                print('Sorry, the guessing number is less than the number')
            elif guess_num > rand_num:
                print('Sorry, the guessing number is greater than the number')
        from calculatgame2 import end_of_program
        end_of_program()
    elif user_input == '2' :
        print('You have 8 chances')
        rand_num = randint(1, 20)
        for i in range(0,8):
            guess_num = int(input('Guess a number ? '))
            if guess_num == rand_num :
                print("Great !! guess right")
            elif guess_num < rand_num :
                print('Sorry, the guessing number is less than the number')
            elif guess_num > rand_num:
                print('Sorry, the guessing number is greater than the number')
        from calculatgame2 import end_of_program
        end_of_program()
    elif user_input == '3' :
        print('You have 10 chances')
        rand_num = randint(1, 20)
        for i in range(0,10):
            guess_num = int(input('Guess a number ? '))
            if guess_num == rand_num :
                print("Great !! guess right")
                break
            elif guess_num < rand_num :
                print('Sorry, the guessing number is less than the number')
            elif guess_num > rand_num:
                print('Sorry, the guessing number is greater than the number')
        from calculatgame2 import end_of_program
        end_of_program()
