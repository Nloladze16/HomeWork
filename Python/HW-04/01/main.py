def main():
    age = int(input("What is your age? "))

    if age < 13:
        print("Child")
    elif age < 20:
        print("Teenager")
    elif age < 65:
        print("Adult")
    else:
        print("Senior")
    pass


if __name__ == "__main__":
    main()


# Ages 0-12: "Child"
# Ages 13-19: "Teenager"
# Ages 20-64: "Adult"
# Ages 65 and above: "Senior"
