def main():

    temp = float(input("Whats temperature? "))

    if temp < 32:
        print("Freezing")
    elif temp < 60:
        print("Cold")
    elif temp < 80:
        print("Mild")
    elif temp < 90:
        print("Warm")
    else:
        print("Hot")


if __name__ == "__main__":
    main()

# Below 32: "Freezing"
# 32-59: "Cold"
# 60-79: "Mild"
# 80-89: "Warm"
# 90 and above: "Hot"
