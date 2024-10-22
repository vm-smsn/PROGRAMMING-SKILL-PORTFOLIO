# Vince Michael J. Samson | ID:04-24-0147
# Exercise 9: Hello
# 9/30/2024

def hello(): # this line of code defines "hello()".
    print("Hello") # within the function contains a single statement "print("Hello").
    
def main(): # this part defines another function named "main" which then calls upon the "hello()" function.
    hello()
    
if __name__ == "__main__":  # this if statement checks if the code is run as the main program.
    main()                  # if the code is True then the "main" function is called.
    