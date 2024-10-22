# Vince Michael J. Samson | ID:04-24-0147
# Exercise 10: Is it even?
# 10/15/2024

number = int(input("Please enter a number: "))
# We ask the user to input a number to determine if it is an odd or an even number
# It then stores the value inside "number"


if number % 2==0: # This checks if the number is divisible by 2 by dividing it and checking if the remainder is 0.
    print("It's even!!! ") # If the given integer activates and makes the function above True, it then displays that the 
    # inputted number is even.
else: # If the inputted integer is turns out to be False it then moves on to the else function.
    print("It's odd!!! ") # If the condition is not met it then displayds that the given number is odd.