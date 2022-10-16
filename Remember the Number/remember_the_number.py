import random
import time
import os

length_of_number = int(input("Enter the length of the random number:"))

placeholder = "a"
placeholder = placeholder * length_of_number
randomized_number = ""

if len(placeholder) == 1:
    first_digit = random.randint(0,9)
    randomized_number = str(first_digit)
    print(randomized_number)

if len(placeholder) > 1:
    for i in range(0, len(placeholder)):
        if i == 0:
            first_digit = random.randint(1,9)
            str_first_digit = str(first_digit) 
            randomized_number = randomized_number + str_first_digit
        if i >= 1:
            more_digits = random.randint(0,9)
            str_more_digits = str(more_digits)
            randomized_number = randomized_number + str_more_digits
    
print(randomized_number)
print("You have five seconds to remember this number.")
print(time.sleep(5))
os.system('cls')

print("Enter the number:")
enter_the_number = int(input(""))
str_enter_the_number = str(enter_the_number)

if str_enter_the_number == randomized_number:
    print("Correct!")
else:
    print("Incorrect. The number was " + randomized_number)
