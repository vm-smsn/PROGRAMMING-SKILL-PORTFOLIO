# Vince Michael J. Samson | ID:04-24-0147
# Exercise 3: Biography
# 9/13/2024

# To be able to get the inputs of the user we will be using 'input'.
# Within the variable we use 'input' function to prompt the user for their data.
firstname = input ("First name: ") # Asks for the user's first name.
surname = input ("Surname: ")      # Asks for the user's surname.
hometown = input ("Hometown: ")    # Asks for the user's hometown.

while True:
    age = input ("Age: ")
    try:
        age = int(age) 
        # The "int" prevents the user from inputting non numerical data (age).
        break
    except ValueError:
        print ("Invalid, please enter a numeric value")   
        # This appears if the user inputs a non numerical data (age).

# Now that we have our variables, we need a place to store the data.
# The input is stored in the person dictionary
userdata = {  # {} is a placeholder or a dictionary
    "First name": firstname,
    "Surname": surname,
    "Hometown": hometown,
    "Age": age,
}
# After acquiring the user's data it is now time to print the information.
# I have used f-strings to eliminate going back and forth witht the code.

# The following print functions displays the data given by the user in order.
print(f"First Name: {userdata['First name']}")
print(f"Surname: {userdata['Surname']}")
print(f"Hometown: {userdata['Hometown']}")
print(f"Age: {userdata['Age']}")