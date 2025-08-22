# Personal Greeting Program
# Ask user for first and last name, format properly, and create greeting


def main():
    """Entry point of the program."""
    # TODO: Get user's first name, remove whitespace and capitalize
    first_name = input("Whats's Your First Name ").title().strip()

    # TODO: Get user's last name, remove whitespace and capitalize
    last_name = input("Whats's Your Last Name ").title().strip()

    # TODO: Print personalized greeting using f-string
    print(f"Hello, {first_name} {last_name}! Welcome to Python programming.")

# Run the main function
main()
