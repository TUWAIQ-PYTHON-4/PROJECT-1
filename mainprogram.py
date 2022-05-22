# main page
class games:
    def __init__(self , name):
        self.name = name
    def get_Making_words_game(self):
        from wordsgame import Making_words_game
        Making_words_game()
    def ger_name(self):
        return self.name
    def set_name(self,name):
        self.name = name
    def get_guessing_game(self):
        from guessgame import guessing_game
        guessing_game()
    def get_calcultion_game(self):
        from calculatgame2 import calcultion_game
        calcultion_game()

game = games('lama') # class for gamer
def start_program():
    game_user = 0
    flag = True
    while flag:
        try:
            game_user = int(input(
                'what the game you want\n[1] If you want calculat game\n[2] If you want words game\n[3] If you want guess game\n[4]If you want exit'))
        except:
            print('This is not a number')

        if game_user == 1:
            game.get_calcultion_game()
        elif game_user == 2:
            game.get_Making_words_game()
        elif game_user == 3:
            game.get_guessing_game()
        elif game_user == 4:
            exit()
        else:
            print('Please enter correct')

start_program()