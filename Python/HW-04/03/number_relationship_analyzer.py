def main():

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if num1 == num2:
        print("The numbers are equal")
    else:
        print("The numbers are not equal")
        if num1 > num2:
            print(f"{num1} is greater than {num2}")
        else:
            print(f"{num2} is greater than {num1}")

    if num1 < 0 and num2 < 0:
        print("Both numbers are negative")
    elif num1 > 0 and num2 > 0:
        print("Both numbers are positive")
    else:
        print("The numbers have mixed signs")


if __name__ == "__main__":
    main()
