# Text Processor
# Various text processing functions


def main():
    """Entry point of the program."""
    # TODO: Get cleaned input from user
    cleaned_text = get_input()

    # TODO: Display all processed versions
    print(f"Cleaned text: {cleaned_text}")
    print(f"Word count: {count_words(cleaned_text)}")
    print(f"Uppercase: {make_uppercase(cleaned_text)}")
    print(f"Lowercase: {make_lowercase(cleaned_text)}")

# TODO: Create get_input() function that gets text input from user
# and returns it cleaned.
def get_input():
    return input("Enter some text: ").strip().title()
   
# TODO: Create count_words(text) function that takes a string
# and returns the number of words.
def count_words(text):
    words = text.split()
    return len(words) 

# TODO: Create make_uppercase(text) function that takes a
# string and returns it in uppercase.
def make_uppercase(text: str):
    return text.upper()

# TODO: Create make_lowercase(text) function that takes a
# string and returns it in lowercase.
def make_lowercase(text: str):
    return text.lower()

# Run the program
main()
