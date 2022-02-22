#Random Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Random Password Generator!")
nr_letters= int(input("How many letters in your password?\n")) 
nr_symbols = int(input(f"How many symbols in your password?\n"))
nr_numbers = int(input(f"How many numbers in your password?\n"))

random_letters = random.sample(letters, nr_letters)
random_symbols = random.sample(symbols, nr_symbols)
random_numbers = random.sample(numbers, nr_numbers)

easy = random_letters + random_symbols + random_numbers
character = ""
for part in easy:
  character += part
#Print in order
# print(character)

#Shuffle password
random.shuffle(easy)
hard_password = ""
for hard_part in easy:
  hard_password += hard_part
print(hard_password)
