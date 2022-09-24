# Calculator
from art import logo

print(logo)
# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multipy
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

continue_calculation = bool()

num1 = float(input("What's the first number?: "))
for symbol in operations:
  print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
num2 = float(input("What's is the second number?: "))
operation = operations[operation_symbol]
first_answer = operation(num1, num2)
  
print(f"{num1} {operation_symbol} {num2} = {first_answer}")

continue_operation = input("Type 'y' to continue calculating with 16, or type 'n' to exit .: ").lower()

if continue_operation == "y":
  continue_calculation = True
elif continue_operation == "n":
  continue_calculation = False

while continue_calculation:
  operation_symbol = input ("Pick another operation : " )
  num3 = float( input ("What's the next number ?: " ) )
  calculation_function = operations [ operation_symbol ]
  second_answer = calculation_function(first_answer , num3)
  print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
  continue_operation = input("Type 'y' to continue calculating with 16, or type 'n' to exit .: ").lower()
  if continue_operation == "y":
    continue_calculation = True
    first_answer = second_answer
  elif continue_operation == "n":
    continue_calculation = False

  
#print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")