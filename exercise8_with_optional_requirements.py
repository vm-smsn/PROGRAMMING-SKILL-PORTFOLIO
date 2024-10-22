# Vince Michael J. Samson | ID:04-24-0147
# Exercise 8: Simple Search
#9/18/2024

# This acts as our library of people which is a variable prompt.
namesofpeople = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# This displays the question that asks for the name of the person.
search_term = input("Enter the name you want to search for: ")

# This command converts the input into lowercase thus allowing non uppercase
# names within the inputted data.
search_term = search_term.lower()  # Convert search term to lowercase

# In this section I created a search loop that iterates throuch each name within
# the list inside namesofpeople.
found = False
for namesofpeople in namesofpeople:
    # ^ This code is a loop that checks the name of people in the list (namesofpeople).
    if namesofpeople.lower() == search_term:  # This code converts the names into lowercase
    # both within the list and the inputted answer.
        found = True # If "found = True" the codes moves on to the next "if" statement 
        break # The "break" ends the loop.
        
# In this area the print display varies if "found = True" or not.
if found:
    print(f"{search_term} is in the list.")
    # if it is True and it is in the list then it will display " ___ is in the list"
else:
    print(f"{search_term} is not in the list.")
    # if it is false then it will say "___ is not in the list"