# function to color the output
def color_this(desired_color, text):
    if desired_color == "blue":
        r= 108
        g= 178
        b= 208
        return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
    elif desired_color == "red":
        r= 224
        g= 0
        b= 48
        return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
    elif desired_color == "yellow":
        r= 224
        g= 203
        b= 48
        return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
    elif desired_color == "green":
        r= 18
        g= 206
        b= 108
        return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
    else:
        return ""

# Welcome Function when the program is started
def welcome(user_name: str):
    print('''

░░     ░░ ░░░░░░░ ░░       ░░░░░░  ░░░░░░  ░░░    ░░░ ░░░░░░░ 
▒▒     ▒▒ ▒▒      ▒▒      ▒▒      ▒▒    ▒▒ ▒▒▒▒  ▒▒▒▒ ▒▒      
▒▒  ▒  ▒▒ ▒▒▒▒▒   ▒▒      ▒▒      ▒▒    ▒▒ ▒▒ ▒▒▒▒ ▒▒ ▒▒▒▒▒   
▓▓ ▓▓▓ ▓▓ ▓▓      ▓▓      ▓▓      ▓▓    ▓▓ ▓▓  ▓▓  ▓▓ ▓▓      
 ███ ███  ███████ ███████  ██████  ██████  ██      ██ ███████ 

    ''')
    print(f"Hello! {user_name}. Welcome to "+ color_this("blue", "I'm feeling") +" music player. \n ")

# song type function
def song_type(index: int):
    if index == 0:
        return "energetic"
    elif index == 1:
        return "happy"
    elif index == 2:
        return "calm"
    elif index == 3:
        return "sad"
    else:
        return "Error! Index in song_type() function is not valid. "


