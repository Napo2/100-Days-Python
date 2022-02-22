print("Check if a number is a prime number\n")

def prime_checker(number):
  prime = True
  for i in range(2, number):
    if number % i == 0:
      prime = False
  if prime:
    print("Not a prime number.") 
  else:
    print("Prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
