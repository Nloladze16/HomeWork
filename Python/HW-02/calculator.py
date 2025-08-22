# Simple Calculator with Functions
# Performs basic mathematical operations using separate functions


def main():
    """Entry point of the program."""
    # TODO: Get two numbers from user
    first_number = float(input("Enter First Number: "))
    second_number = float(input("Enter Second Number: "))

    # TODO: Perform all operations and display results formatted to 2 decimal places
    print(f"Addition: {add(first_number,second_number):.2f}")
    print(f"Subtraction: {subtract(first_number,second_number):.2f}")
    print(f"Multiplication: {multiply(first_number,second_number):.2f}")
    print(f"Division: {divide(first_number,second_number):.2f}")

# TODO: Create add(x, y) function that returns sum of x and y
def add(x,y):
    return x + y
    
# TODO: Create subtract(x, y) function that returns the difference of x and y
def subtract(x,y):
    return x - y

# TODO: Create multipy(x, y) function that returns the product of x and y
def multiply(x, y): 
    return x * y

# TODO: Create divide(x, y) function that returns the quotient of x and y
def divide(x, y):
    return x / y

# Run the program
main()
