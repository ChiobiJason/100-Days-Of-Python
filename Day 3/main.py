print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# Control Flow
if height >= 120:
  age = int(input("What is your age? "))
  if age < 12:
    price = 5
  elif age >= 12 and age <= 18:
    price = 7
  else:
    price = 12
  photo = input("Do you want a photo? Y or N ")
  if photo == "Y" or photo == "y" or photo == "Yes" or photo == "yes":
    print(f"You can ride the rollercoaster for ${price + 3}")
  else:
    print(f"You can ride the rollercoaster for ${price}")
else:
	print("Sorry you have to grow taller before you can ride.")