#Password Generator Project
import random 
import string
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
letters=list(string.ascii_lowercase+string.ascii_uppercase)
numbers=list(str(range(1,10)))
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letter_count=0
symbol_count=0
number_count=0
totchar=nr_letters+nr_symbols+nr_numbers
password=[]
if letter_count==nr_letters and symbol_count==nr_symbols and number_count==nr_numbers:
  print(f"Your password is: {password}")
else:
  for lets in range(0,nr_letters):
    password+=letters[random.randint(0,len(letters)-1)]
  for nums in range(0,nr_numbers):
    password+=numbers[random.randint(0,len(numbers)-1)]
  for lets in range(0,nr_symbols):
    password+=letters[random.randint(0,len(symbols)-1)]


random.shuffle(password)
password=''.join(password)
print(f"Your suggested password is {password}")

    