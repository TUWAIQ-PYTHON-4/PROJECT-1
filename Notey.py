import myCalendar  as c
 
class Mian :
 '''
   program let users save ,update,delete,search their notes and show calendar
 '''
 Note = {}
 def Typing(self,title:str,note:str):
  '''
  function takes two parameters (key,value) then saves it in dictionary 
  '''
  Mian.Note[title] = note
 def update(self,title:str,note:str):
  '''
  function takes two parameters (key,value) then update it in dictionary 
  '''    
  Mian.Note.update({title: note})
 def Search(self,title:str):
    '''
    function takes one parameters (key) then return value 
    '''
    return Mian.Note.get(title)
 def Delete(self,title:str):
    '''
    function  takes one parameters (key) then delete it from dictionary
    '''
    Mian.Note.pop(title)
 def printAll(self):
   '''
    function dosen't take  parameter  but return    dictionary
   '''
   #my_cubes = list(filter(lambda values: None, Mian.Note))  
   return Mian.Note
 def printAllTitles(self):
   '''
    function dosen't take  parameter  but print    all titles
   '''
   print (list(filter(lambda x:True, list(Mian.Note))))

print ("Welcome to my program ")
print ("This is note program it let you type,update,delete and show your note easily")
print("the options:")
print("1 to type a note")
print("2 to update a note ")
print("3 to delete a note")
print("4 to show all notes")
print("5 to show a calendar")
print("6 to search a note")
print("7 to show all titles")
print("0 to exit")
print("")
option = int(input())
try:
 while option != 0:
   if option ==1:
     title = input("title: ")
     print()
     note = input("note: ")  
     Mian().Typing(title,note)
     option=-1
   elif option==2:
     title = input("title: ")
     print()
     note = input("note: ")  
     Mian().update(title,note)
     option=-1
   elif option==3:
     title = input("title: ")
     Mian().Delete(title)
     option=-1
   elif option==4:
     print(Mian().printAll())
     option=-1
   elif option==5:
      c.calendar2022()
      option=-1 
   elif option==6:
      title = input("title: ")
      print()
      print(Mian().Search(title))
      option=-1         
   elif option==7:
      print(Mian().printAllTitles())
      option=-1               
   elif option==0:
      break;
   elif option not in range(0,7) :
      print("")
      print("the options:")
      print("1 to type a note")
      print("2 to update a note ")
      print("3 to delete a note")
      print("4 to show notes")
      print("5 to show a calendar")
      print("6 to search a note")
      print("7 to show all titles")
      print("0 to exit")
      print("")
      option = int(input())
except Exception as ve:
    print(ve)
else:
    print("thank u ")

