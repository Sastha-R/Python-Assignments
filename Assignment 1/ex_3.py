Balance = 100000
pin = "123"
attempt = 1

def check_Balance():
    global Balance
    print("Balance : ",Balance)

def Deposit():
    global Balance
    amt = int(input("enter amount : "))
    if amt > 0:
        Balance += amt
        print("Deposited")
    else:
        print("enter valid amt")

def WithDraw():
    global Balance
    amt = int(input("enter amt:"))
    if(Balance >= amt):
        Balance -= amt
    else:
        print("insuffient balance")

def pin_change():
    global pin
    global attempt
    if(attempt > 3):
        entered_pin = input("Enter current PIN: ")
        if entered_pin == pin:
            pin = input("Enter new PIN: ")
            print("PIN changed")
        else:
            attempt += 1
            print("Wrong PIN")


while(True):
    print("enter your choice: ")
    ch = int(input("1. Check Balance 2. Deposit 3. Withdraw 4. Change PIN 5. Exit "))
    match ch:
        case 1:
            check_Balance()
        case 2:
            Deposit()
        case 3:
            WithDraw()
        case 4:
            pin_change()
        case 5 :
            print("exiting")
            break
            
        