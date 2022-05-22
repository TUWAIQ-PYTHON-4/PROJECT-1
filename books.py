

class UsedBooks:
    
    def __init__(self, name, genre, price, rating, summuray, condition):
        self.__name = name
        self.__genre = genre
        self.__price = price
        self.__rating = rating
        self.__summuray = summuray
        self.__condition = condition
    
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def set_genre(self, genre):
        self.__genre = genre

    def get_genre(self):
        return self.__genre

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price
    
    def set__rating(self,rating):
        self.__rating = rating

    def get__rating(self):
        return self.__rating

    def set__summuray(self, summuray):
        self.__summuray = summuray

    def get__summuray(self):
        return self.__summuray

    def set__condition(self, condition):
        self.__summuray = condition

    def get__condition(self):
        return self.__condition


book1 = UsedBooks('Harry Potter and the Chamber of Secrets', 'Children books',4.19, 4.5, "All Harry Potter wanted was to get back to the Hogwarts School for Witchcraft and Wizardry.But he receives a warning if he returns disaster will strike." ,'Very Good')
book2= UsedBooks('The Secret Garden','Children books', 6.40, 4,"An orphaned girl discovers a magical garden hidden at her strict uncle's estate.", 'Good')
book3= UsedBooks('Long Walk to Freedom: The Autobiography of Nelson Mandela', 'History', 4.19, 4.5, "Nelson Mandela: an international hero whose lifelong dedication to the fight against racial oppression in South Africa",'Good')


