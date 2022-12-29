class CustomException(Exception):
  def __init__(self, message):
    self.message = message

list_a = [1, 2, 3, 4, 5]
index = input("Enter the index = ")
try:
  index = int(index)


  x = list_a[index]
except IndexError:

  raise CustomException(f"The index {index} is incorrect and index should lie between -{len(list_a)} and {len(list_a) - 1}")
except ValueError:
 
  raise CustomException("Use an Integer value as the input.")
