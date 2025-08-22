# Number Formatter
# Formats large numbers with commas and shows rounded version


def main():
    """Entry point of the program."""
    # TODO: Get a large number from user
    number = int(input("Enter a Large Number: "))

    # TODO: Display original number with comma formatting
    print(f"Original number: {format_number(number)}")

    # TODO: Round to nearest thousand and display
    print(f"Rounded to nearest thousand: {format_number(round(number, -3))}")

# TODO: Create function format_number(number)
def format_number(number):
    """Take a number and return it formatted with commas."""
     
    return f"{number:,}"

# Run the program
main()
