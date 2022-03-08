logo = """
 _____                       _   _                                  _               
|  __ \                     | | | |                                | |              
| |  \/_   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_| 
"""
import random
def clear():
"""Clears the screen"""
os.system('cls' if os.name == 'nt' else 'clear')

random_number = random.randint(1, 100)
guesses = 0

def compare(random_number, guess):
  """Compares the random integer and guessed number"""
  if random_number > guess:
    return "Too low."
    return "Guess again."
  elif guess > random_number:
    return "Too high."
    return "Guess again"
  else:
    return "You guessed correctly!"

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
  guesses = 10
elif difficulty == "hard":
  guesses = 5
else:
  guesses = 0
  print("Please enter a valid selection")

while guesses != 0:
  print(f"You have {guesses} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  print(compare(random_number, guess))
  if guess == random_number:
    guesses = 0
  else:
    guesses -= 1
