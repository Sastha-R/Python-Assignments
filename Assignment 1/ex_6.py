username = "tuco"
password = "777"

attempts = 3

while attempts >= 1:

    new_username = input("Enter username: ")
    new_password = input("Enter password: ")

    if new_username == username and new_password == password:
        print("Login successful")
        break

    else:
        attempts -= 1
        print("Invalid username or password")
        print("Remaining attempts:", attempts)

        if attempts <= 0:
            print("Account locked")