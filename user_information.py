


class information_about_product():
     def __init__(self , python,java ) :
      self.python = python
      self.java = java

     enter_thebook=str(input("information about : "))
     if enter_thebook=="python":
           print("The book consists of 200 pages. Features of the book After reading it, you will master the python language easily")  
     elif enter_thebook=="java":
          print("The book consists of 300 pages. Features of the book After reading it, you will master the Java language easily") 
     elif enter_thebook=="javascript":
          print("The book consists of 400 pages. Features of the book After reading it, you will master the Javascript language easily") 
     elif enter_thebook=="php":
          print("The book consists of 500 pages. Features of the book After reading it, you will master the php language easily") 
     elif enter_thebook==".net":
          print("The book consists of 500 pages. Features of the book After reading it, you will master the php language easil") 
     elif enter_thebook :
          print("sorry we don't hava")
          
#bb=information_about_product(p)

'''

     def __init__(self):
      self.python = input('what do you want to information about ')
         
     def show_full_name(self):
          return self.python +"444 pages"

     def __init__(self):
      self.java = input('what do you want to information about ')
         
     def show_full_name(self):
       return self.java +"555 pages"

inform_product =information_about_product()
print(inform_product.show_full_name())
'''

