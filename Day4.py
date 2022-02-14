rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

player_choice = input("What do you chose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")

player = [rock, paper, scissors]


# Rock = 0
# Paper = 1
# Scissors = 2

pci = player[int(player_choice)]

print(pci)

computer = [rock, paper, scissors]
cc = random.choice(computer)

print(f"Computer Chose: \n{cc}")

if pci == rock and cc == paper:
  print("You lose.")
elif pci == rock and cc == scissors:
  print("You win!")
elif pci == rock and cc == rock:
  print("Tie, try again.")
elif pci == paper and cc == rock:
  print("You win!")
elif pci == paper and cc == paper:
  print("Tie, try again.")
elif pci == paper and cc == scissors:
  print("You lose.")
elif pci == scissors and cc == rock:
  print("You lose.")
elif pci == scissors and cc == paper:
  print("You win!")
elif pci == scissors and cc == scissors:
  print("Tie, try again.")
