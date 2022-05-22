# page calculate game
import time
from threading import Timer
from random import randint , random ,choice
import operator
ops = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
timeout = 60

def end_of_program():
    print('If you want play again enter [1]\nIf you want return to main page enter [2]\nIf you want exit enter [3]')
    while True:
        next_step = int(input())
        if next_step == 1:
            calcultion_game()
        elif next_step == 2:
            from mainprogram import start_program
            start_program()
        elif next_step == 3:
            exit()
        else:
            print('Please enter correct number')

def calcultion_game():
    print("Enter the number of the level that you want: \n [1] for Hard level \n [2] for Medium level \n [3] for Easy level")
    while True :
        user_input = input()
        if user_input == '1':
            print("You have %d seconds to complete the exercise...\n" % timeout)
            for number_answer in range(0, 10):
                number1 = randint(10, 20) #take a random number
                number2 = randint(10, 20)
                operation = choice(list(ops.keys()))
                equation = lambda number1,number2 :ops.get(operation)(number1, number2) #Eqation comosition
                answer = equation(number1,number2)
                answer = round(answer,2) #rounding number
                while True:
                    print( number1, operation, number2, ' = ')
                    t = Timer(timeout, print, ['Sorry, times up'])
                    t.start() #start timer
                    answer_user = input()
                    t.cancel()#end timer
                    answer_user = float(answer_user)
                    if answer_user == answer:
                        print('great !!')
                    else:
                        print("Incorrect answer")
                    break
            print("Good Job")
            end_of_program()
        elif user_input == '2':
            print("You have %d seconds to complete the exercise...\n" % timeout)
            for number_answer in range(0, 10):
                number1 = randint(5, 15)
                number2 = randint(5, 15)
                operation = choice(list(ops.keys()))
                equation = lambda number1, number2: ops.get(operation)(number1, number2)
                answer = equation(number1, number2)
                answer = round(answer, 2)
                while True:
                    print( number1, operation, number2, ' = ')
                    t = Timer(timeout, print , ['Sorry, times up'])
                    t.start()
                    answer_user = input()
                    t.cancel()
                    answer_user = float(answer_user)
                    if answer_user == answer:
                        print('great !!')
                    else:
                        print("Incorrect answer")
                    break
            print("Good Job")
            end_of_program()
        elif user_input == '3':
            print("You have %d seconds to complete the exercise...\n" % timeout)
            for number_answer in range(0, 10):
                number1 = randint(0, 10)
                number2 = randint(1, 10)
                operation = choice(list(ops.keys()))
                equation = lambda number1, number2: ops.get(operation)(number1, number2)
                answer = equation(number1, number2)
                answer = round(answer, 2)
                while True:
                    print( number1, operation, number2, ' = ')
                    t = Timer(timeout, print, ['Sorry, times up'],)
                    t.start()
                    answer_user = input()
                    t.cancel()
                    answer_user = float(answer_user)
                    if answer_user == answer:
                        print('great !!')
                    else:
                        print("Incorrect answer")
                    break
            print("Good Job")
            end_of_program()
        elif user_input.isalpha():
            print('please enter number')
        else:
            print("please enter right number")
