accounts = []


def create_account():
    account_number = input("Enter Account Number: ")
    name = input("Enter Name: ")
    balance = float(input("Enter Initial Deposit: "))

    if balance < 0:
        print("Initial deposit cannot be negative.")
        return

    account = {
        "account_number": account_number,
        "name": name,
        "balance": balance,
        "transactions": []
    }

    accounts.append(account)

    print("Account created")


def find_account(account_number):
    for account in accounts:
        if account["account_number"] == account_number:
            return account

    return None


def deposit():
    account_number = input("Enter Account Number: ")

    account = find_account(account_number)

    if account is None:
        print("Account not found.")
    else:
        amount = float(input("Enter Deposit Amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
        else:
            account["balance"] += amount

            account["transactions"].append(
                "Deposited: " + str(amount)
            )

            print("Amount deposited")


def withdraw():
    account_number = input("Enter Account Number: ")

    account = find_account(account_number)

    if account is None:
        print("Account not found.")
    else:
        amount = float(input("Enter Withdrawal Amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
        elif amount > account["balance"]:
            print("Insufficient balance.")
        else:
            account["balance"] -= amount

            account["transactions"].append(
                "Withdrawn: " + str(amount)
            )

            print("Amount withdrawn")


def check_balance():
    account_number = input("Enter Account Number: ")

    account = find_account(account_number)

    if account is None:
        print("Account not found.")
    else:
        print("Account Holder:", account["name"])
        print("Balance:", account["balance"])


def transaction_history():
    account_number = input("Enter Account Number: ")

    account = find_account(account_number)

    if account is None:
        print("Account not found.")
    elif not account["transactions"]:
        print("No transactions found.")
    else:
        print("\nTransaction History")

        for transaction in account["transactions"]:
            print(transaction)


while True:

    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            create_account()

        case 2:
            deposit()

        case 3:
            withdraw()

        case 4:
            check_balance()

        case 5:
            transaction_history()

        case 6:
            print("exited")
            break

        case _:
            print("Invalid choice.")



