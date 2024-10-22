# Vince Michael J. Samson | ID:04-24-0147
# Exercise 6: Brute Force Attack
# 9/13/2024
        
correct_password = "_.Michael@Pogi._"
# This is the variable that holds the correct password that needs to be inputted by the user.
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    password_input = input("Enter the password: ")
    # The while True function loops until the correct password is inputted.
    if password_input == correct_password:
        # The if statement checks if the input corresponds to the variable (correct_password).
        print("Correct password!")
        break
    # The break function allows us to exit the loop once the correct password has been inputted.
    else:
        print(f"Incorrect password. You have {max_attempts - attempts - 1} attempts left.")
        attempts += 1
        # This prints if ever the user has typed the wrong password.
        
if attempts == max_attempts:
    print("Maximum attempts reached. Authorities have been alerted.")
    # If the maximum limits has been reached it will then alert the authorities about the
    # brute force attack on the account.