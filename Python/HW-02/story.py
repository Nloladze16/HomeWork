# Interactive Story Generator
# Creates a personalized story based on user input


def main():
    """Entry point of the program."""
    # TODO: Get user information
    name = input("What's your name? ").title().strip()
    age = int(input("What's your age? "))
    color = input("What's your favourite color? ").strip()
    # TODO: Generate and display the story
    print(create_story(name,age,color))

# TODO: add parameters to create_story() function and fill complete story
def create_story(name,age,color):
    """Create and return a story string using the provided parameters"""
    story = f"""Here's your story:
                Once upon a time, there was a person named {name} who was {age} years old. 
                {name} loved the color {color} so much that everything in their house was {color} !
                The end.
            """
    return story


# Run the program
main()
