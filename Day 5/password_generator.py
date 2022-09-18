import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = []

# For letters
for x in range(nr_letters):
  random_number = random.randrange(0, (len(letters)))
  password.append(letters[random_number])

# For Symbols
for x in range(nr_symbols):
  random_number = random.randrange(0, (len(symbols)))
  password.append(symbols[random_number])

# For Numbers
for x in range(nr_numbers):
  random_number = random.randrange(0, (len(numbers)))
  password.append(numbers[random_number])

print(password)

random.shuffle(password)

i = ""
for x in password:
    i += x

print(password)
print(i)