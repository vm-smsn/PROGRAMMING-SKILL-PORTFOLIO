# Vince Michael J. Samson | ID:04-24-0147
# Exercise 5: Days of the Month
# 9/13/2024

# We first need to create a dictionary for the months.
days_in_month = {
    1: 31,  # January
    2: 28,  # February (assuming a non-leap year)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}

# After making a dictionary we need a place to store the values that 
# will be inputted by the user. 
month_number = int(input("Enter the month of your choice (1-12): "))
# This asks the user to enter a month number between 1-12 and then stores the value in
# the month_number variable.
year = int(input("Enter the year of your choice: "))
# This asks the user to enter any year of their choice, it then stores that 
# value within the variable "year".

if 1 <= month_number <= 12: # Chechks if the inputted number is within range of 1-12.
    print(f"There are {days_in_month[month_number]} days in month {month_number}.")
    # It then proceeds to display
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
    # Asks the user for a valid number within the range (1-12).
def is_leap_year(year):
    # This function allows us to call upon anything within the dictionary "{}".
    # It is a more convenient way to display an outcome rather than writing a code for each one.
    if year % 4 == 0: # This calculates if the year is divisible by 4
    # thus allowing it to be a potential leap year
        if year % 100 == 0:
            if year % 400 == 0:
                # If the inputted year is divisible by 100 then it is not a leap year
                # unless it is also divisible by 400.
                return True
            else:
                return False
            # If the function returns as True if it is a leap year and False if it is not.
        else:
            return True
    else:
        return False
  # If it is invalid, the code then is set to display an error message. 
