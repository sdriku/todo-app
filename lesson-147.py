import random

try:
    user_input_lower = int(input('Enter the lower bound: '))
    user_input_upper = int(input('Enter the upper bound: '))
except ValueError:
            print('Your command is not valid, please enter a whole number')


# Generate a random whole number between 1 and 10 (inclusive)
try:
    random_number = random.randint(user_input_lower + 1, user_input_upper - 1)
    print(random_number)
except ValueError:
            print(f"There is no whole number between {user_input_lower} and {user_input_upper}.")


# Your task is to create a program that generates a random whole number.
#  The program first asks the user to enter a whole number. Then, once the user enters a number, the program asks the user again to enter another number.
# Then, the program returns a random number that falls between the two whole numbers. 