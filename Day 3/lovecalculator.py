name1 = input("What is you name? ").lower()
name2 = input("What is your wife's name? ").lower()

name = name1 + " " + name2

# Check for TRUE
first_digit = str(name.count("t") + name.count("r") + name.count("u") + name.count("e"))

# Check for LOVE
second_digit = str(name.count("l") + name.count("o") + name.count("v") + name.count("e"))

# Join digits and turn to an integer
score = int(first_digit + second_digit)

# Check conditions
if score <= 10 or score >= 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
