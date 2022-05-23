'''

## Based on what you've learned until now , create a project of your choosing (impress us with your imagination).
This project must at least satisfy the following minimum requirements :

- Must be interactive on CLI. (COMMAND LINE INTERFACE)
- Use lists or dictionaries or tuples. 
- Use loops.
- Use functions that return an output . 
- Use a Lambda function.
- Use at least 1 Class.
- Use some form of Error Handling .
- Organize Your Code into modules & (or packages)


'''

# CLI (COMMAND LINE INTERFACE )
def person_name():
    user_input = input('Enter Your Name To Added On Your Car ==> ? ')
    
# EXCEPTION HANDLING
    if not type(user_input) is str:
        raise Exception("Only String are allowed")
        
# CLASS
class Car_details:
    def __init__(self, name, model ):
      self.name = name
      self.model = model


      '''
      def showCar(self):
        pass
      '''

# TAKE OBJECT OF THE CLASS
car1 = Car_details('lexus','2021')
car2 = Car_details('mazda','2016')

# MAKE A LIST 
list = [car1.name,car2.name]

#USE LOOP 
for i in range(len(list)):
     print(list[i])