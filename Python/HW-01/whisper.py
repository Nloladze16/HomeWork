
def main():
    # TODO: Get input from the user

    text = input("Type Something Here ")
   
    # TODO: Process the text using whisper function
    text = whisper(text)
    
    # TODO: Print the result
    print(text)
    pass


# TODO: Create whisper function that takes text as parameter
def whisper(text):

    text =  text.casefold()
    text =  text.replace("!","")

    # TODO: Convert to lowercase and remove all exclamation marks
    # TODO: Return the processed text
    return text
    pass


if __name__ == "__main__":
    main()
