# Function Practice
# Demonstrates various function concepts including default parameters


def main():
    """Entry point of the program."""
    # TODO: Get a number from user
    user_number = int(input("Enter a number: "))

    # TODO: Display square and cube
    print(f"{user_number} Squared is {square(user_number):.1f}")
    print(f"{user_number} Cubed is {cube(user_number):.1f}")

    # TODO: Demonstrate default greeting
    print("Default greeting: ", end="")
    greet()
    # print(f"Default greeting: {greet()}")

    # TODO: Get name for personal greeting
    name = input("Enter your name for personal greeting: ")
    print("Personal greeting: ",end="" )
    greet(name)
# TODO: Create square(number) function that takes a number
# and returns its square
def square(number):
    return number * number


# TODO: Create cube(number) function that takes a number
# and returns its cube
def cube(number):
    return number * number * number

# TODO: greet(name="friend") function that prints a greeting
# with default parameter value
def greet(name="friend"):
   print(f"Hello, {name}")
   
     

# Run the program
main()
