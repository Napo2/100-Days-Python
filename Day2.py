bill = input("Welcome to the tip calculator\nWhat was the total bill? $")

percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")

people = input("How many people to split the bill? ")

bill_int = float(bill)
percent_int = float(percentage) 
people_int = float(people)

percent_end = percent_int / 100
bill_end = bill_int * percent_end

total = (bill_int + bill_end) / people_int

#2 ways to do this
total_rounded = "{:.2f}".format(total)
# total_rounded = round(total, 2)

print(f"Each person should pay: ${total_rounded}")
