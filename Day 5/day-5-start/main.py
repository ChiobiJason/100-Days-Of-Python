# fruits = [" Apple ", " Peach ", " Pear "]

# for fruit in fruits:
#   print(fruit)

# i = 1
# while i <= 10:
#   print(i)
#   i += 1

# student_heights = [180, 124, 165, 173, 189, 169, 146]

# start = 0
# count = 0

# for heights in student_heights:
#   start += heights
#   count += 1

# print(round(start / count))

# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# highest_score = 0

# for scores in student_scores:
#   if scores > highest_score:
#     highest_score = scores

# print(f"The highest score in the class is: {highest_score}")

# i = 0
# for x in range(1, 101):
#   i += x

# print(i)

# even_sum = 0
# for x in range(2, 101, 2):
#   even_sum += x

# print(even_sum)

# FizzBuzz

for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
