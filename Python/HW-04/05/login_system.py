def main():
    username = input("Username: ")
    password = input("Password: ")

    if (
        (username == "admin" and password == "password123")
        or (username == "user" and password == "mypass")
        or (username == "guest" and password == "welcome")
    ):
        print("Login successful!")

    elif username != "admin" and username != "user" and username != "guest":

        print("Username not found.")

    elif password != "password123" and password != "mypass" and password != "welcome":
        print("Incorrect password.")


if __name__ == "__main__":
    main()
