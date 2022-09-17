import random

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
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice == 0 or choice == 1 or choice == 2:
  random_number = random.randint(0, 2)

  print("You chose:")
  if choice == 0:
    print(rock)
  elif choice == 1:
    print(paper)
  elif choice == 2:
    print(scissors)

  print("Computer chose:")
  if random_number == 0:
    print(rock)
  elif random_number == 1:
    print(paper)
  elif random_number == 2:
    print(scissors)

  if choice == 0 and random_number == 0:
    print("It's a draw")
  elif choice == 1 and random_number == 1:
    print("It's a draw")
  elif choice == 2 and random_number == 2:
    print("It's a draw")
  elif choice == 0 and random_number == 1:
    print("You lose")
  elif choice == 1 and random_number == 0:
    print("You win")
  elif choice == 0 and random_number == 2:
    print("You win")
  elif choice == 2 and random_number == 0:
    print("You lose")
  elif choice == 1 and random_number == 2:
    print("You lose")
  elif choice == 2 and random_number == 1:
    print("You win")
  elif choice == 2 and random_number == 2:
    print("It's a draw")
else:
  print("You choose an Invalid Number, restart game!")