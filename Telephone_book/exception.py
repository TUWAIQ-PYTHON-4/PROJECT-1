def check_number(input_num:int):
  if input_num < len(10) :
              
   raise Exception("Please write the correct number")

  try:
   check_number(input_num)
  except Exception as err:
   print(err)