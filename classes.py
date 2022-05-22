# class
class User:
    def __init__(self, user_name, id, song_type):
        self.user_name= user_name
        self.id= id
        self.song_type= song_type

    #getter functions
    def username(self):
        return self.user_name

    def id(self):
        return self.id
    
    def song_type(self):
        return self.song_type

    # a function to display fav song type 
    def display_fav_type(self):
        print(self.user_name+"'s favourite song type: \n")
        print(self.song_type+"\n")
