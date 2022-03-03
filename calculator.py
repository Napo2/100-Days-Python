import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
logo = """
 _____________________
|  _________________  |
| | NapoCalc     0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def multiply(n1, n2):
  return n1 * n2
def divide(n1, n2):
  return n1 / n2

#Operations Dictionary
operations = {
  "+": add, 
  "-": subtract, 
  "*": multiply, 
  "/": divide,
}

def calculator_thing():
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  operation_symbol = input("Pick an operation from the list above: ")
  
  num2 = float(input("What's the second number?: "))
  calculation_function = operations[operation_symbol]
  first_answer = calculation_function(num1, num2)
  print(f"{num1} {operation_symbol} {num2} = {first_answer}")
  
  keep_going = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to exit.").lower()
  
  next_answer = first_answer
  
  while keep_going != "n":
    continue_answer = next_answer
    operation_symbol = input("Pick an operation: ")
    continue_num = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    next_answer = calculation_function(continue_answer, continue_num)
    print(f"{continue_answer} {operation_symbol} {continue_num} = {next_answer}")
    keep_going = input(f"Type 'y' to continue calculating with {next_answer}, or type 'n' to exit.").lower()
  else:
    replay = input(print("Would you like to start a new calculation? y/n")).lower()
    if replay == "n":
      print("Thanks for using NapoCalc!")
    else:
      clear()
      calculator_thing()

print(logo)
calculator_thing()
