# imports 
from curses.ascii import isdigit
from functions import welcome, color_this, song_type
from classes import User
import playsound
import random 
import string

'''
Note: must install in the terminal the following to play the sounds on (Mac OS):
pip3 install playsound
pip3 install PyObjC

'''

# Ask about the user name
user_name= input("\nEnter your name: ")

# Generate an ID for user
user_id= input("I'm the user # ")
# lambda function for ID
func= lambda a,b: a+b
a=random.randint(1,9)
b=random.randint(1,9)
user_id_generator = str(random.choice(string.ascii_letters)) + str(random.choice(range(0,9))) + str(user_id) + str(func(a,b))
print("UserID: "+user_id_generator)

welcome(user_name)

print(color_this("yellow",'Note: to exit the program, write the letter “ E ” when asked.\n'))
exit_program = " "
print("""

I am here to check your current mood before listening to any song.
Your mood could be:
1- Happy
2- Calm
3- Sad
4- Energetic

The song will be picked randomly based on your current mood.
Answer the following 20 questions with 'y' for yes and 'n' for no.

""")


#list with expressions/questions
energetic_list= ["I feel like a superhero.", "I am full of energy.", "I feel like going out and exercise.", "I slept well last night.", "I ate well."]
happy_list= ["I am satisfied with my life.", "I feel grateful for the blessings.", "I am living the moment.", "I have accomplished so many goals.", "I feel positive more than negative."]
calm_list= ["I feel like listening more than talking.", "I want to be left alone.", "I am an easy-going and relaxed person.", "I like to invest on myself.", "I feel like I have made mindful decisions and wise choices so far."]
sad_list= ["I do not know anyone I could trust.", "I live in a depressing environment.", "I cannot rely on anyone.", "I am feeling gloomy.", "I feel overwhelmed by work or studies."]
 
q_answer=''


while exit_program != 'E':
    # counters of each classification to keep track of (yes) answers
    energetic_counter=0
    happy_counter=0
    calm_counter=0
    sad_counter=0
    i=1
    for expression in energetic_list:
        while True:
            q_answer= input(str(i)+" - "+expression).lower()
            if q_answer == 'y' :
                energetic_counter+=1
                break
            elif q_answer == 'n':
                energetic_counter+=0
                break
            else: 
                print("Not a valid answer! Try again ")
        i+=1

    i=6  
    for expression in happy_list:
        while True:
            q_answer= input(str(i)+" - "+expression).lower()
            if q_answer == 'y' :
                happy_counter+=1
                break
            elif q_answer == 'n':
                happy_counter+=0
                break
            else: 
                print("Not a valid answer! Try again ")
        i+=1
    
    i=11
    for expression in calm_list:
        while True:
            q_answer= input(str(i)+" - "+expression).lower()
            if q_answer == 'y' :
                calm_counter+=1
                break
            elif q_answer == 'n':
                calm_counter+=0
                break
            else: 
                print("Not a valid answer! Try again ")
        i+=1

    i= 16
    for expression in sad_list:
        while True:
            q_answer= input(str(i)+" - "+expression).lower()
            if q_answer == 'y':
                sad_counter+=1
                break
            elif q_answer == 'n':
                sad_counter+=0
                break
            else: 
                print("Not a valid answer! Try again ")
        i+=1

    # done with the 20 questions

    # list of counter to find the max and index of max value
    counter= [energetic_counter, happy_counter, calm_counter, sad_counter]
    max_counter= max(counter)

    max_index= counter.index(max_counter)

    print(" \n ")

    #start playing

    # generating random integers
    rand1= random.randint(1, 3) # generating either 1,2,or 3

    try:
        song_type = song_type(max_index)
    except TypeError:
        print("The Music player crashes! so bad. \n")
        break

    # code to play a song based on song type.

    # start
    print(color_this("green", "The song is playing . . ♪  ♫ ♪ ♬ "))

    if song_type == "calm":
        print(f"Based on your current mood, the song type is {song_type}. \n")

        if rand1==1:
            print("Your randomly picked song is: \nBillie Eilish - Ocean Eyes")
            playsound.playsound('songs/Calm/Billie Eilish - Ocean Eyes .mp3')
        elif rand1==2:
            print("Your randomly picked song is: \nCalum Scott - You Are The Reason")
            playsound.playsound('songs/Calm/Calum Scott - You Are The Reason.mp3')
        else:
            print("Your randomly picked song is: \nWhitney Houston - Greatest Love of All")
            playsound.playsound('songs/Calm/Whitney Houston - Greatest Love of All.mp3')
    elif song_type == "energetic":
        print(f"Based on your current mood, the song type is {song_type}. \n")

        if rand1==1:
            print("Your randomly picked song is: \nGym Class Heroes - Stereo Hearts")
            playsound.playsound('songs/Energetic/Gym Class Heroes - Stereo Hearts.mp3')
        elif rand1 ==2:
            print("Your randomly picked song is: \nDavid Guetta - Titanium ft. Sia")
            playsound.playsound('songs/Energetic/David Guetta - Titanium ft. Sia.mp3')
        else:
            print("Your randomly picked song is: \nJustin Timberlake- Can't Stop the Feeling!")
            playsound.playsound("songs/Energetic/Justin Timberlake- Can't Stop the Feeling!.mp3")
    elif song_type == "happy":
        print(f"Based on your current mood, the song type is {song_type}. \n")

        if rand1==1:
            print("Your randomly picked song is: \nZayn Ft Zhavia Ward - A Whole New World")
            playsound.playsound('songs/Happy/Zayn Ft Zhavia Ward - A Whole New World.mp3')
        elif rand1==2:
            print("Your randomly picked song is: \nLa La Land - City of Stars")
            playsound.playsound('songs/Happy/La La Land - City of Stars.mp3')
        else:
            print("Your randomly picked song is: \nThe Greatest Showman - A Million Dreams")
            playsound.playsound('songs/Happy/The Greatest Showman - A Million Dreams.mp3')
    else:
        print(f"Based on your current mood, the song type is {song_type}. \n")
        if rand1==1:
            print("Your randomly picked song is: \nAdele - Someone Like You")
            playsound.playsound('songs/Sad/Adele - Someone Like You.mp3')
        elif rand1 ==2:
            print("Your randomly picked song is: \nCalum Scott - No Matter What")
            playsound.playsound('songs/Sad/Calum Scott - No Matter What.mp3')
        else:
            print("Your randomly picked song is: \nEd Sheeran - All Of The Stars")
            playsound.playsound('songs/Sad/Ed Sheeran - All Of The Stars.mp3')

    # end
    print(color_this("red", "The song stopped playing."))

    fav_song_input=input("Do you like the played song type? must answer 'y' or 'n'.")
    if fav_song_input == 'y':
        user_obj= User(user_name,user_id_generator,song_type)
        user_obj.display_fav_type()
        break
    elif fav_song_input == 'n':
        print("You don't have favorate song type yet!")
        break
    else:
        print("Not a valid answer")
    

    #end playing
    exit_program = input("Do you want to exit the program?? answer 'E' to exit. \nOtherwise, you will take the test again. \n")
    

print("The music player is closed. See you later! ")
