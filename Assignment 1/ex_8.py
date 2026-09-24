
def check_even_odd(num):
    print("Even" if num % 2 == 0 else "Odd")


def check_prime(num):
    if num < 2:
        print("Not Prime")
    else:
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            print("Prime")
        else:
            print("Not Prime")


def check_palindrome(num):
    reverse = int(str(num)[::-1])

    if num == reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")


def check_armstrong(num):
    count = len(str(num))

    temp = num
    armstrong_sum = 0

    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** count
        temp //= 10

    if armstrong_sum == num:
        print("Armstrong")
    else:
        print("Not Armstrong")


def reverse_number(num):
    reverse = int(str(num)[::-1])
    print("Reverse:", reverse)


def sum_of_digits(num):
    temp = num
    digit_sum = 0

    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        temp //= 10

    print("Sum of digits:", digit_sum)


num = int(input("Enter a number: "))

while True:

    print("1. Check Even/Odd")
    print("2. Check Prime")
    print("3. Check Palindrome")
    print("4. Check Armstrong")
    print("5. Reverse Number")
    print("6. Sum of Digits")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            check_even_odd(num)

        case 2:
            check_prime(num)

        case 3:
            check_palindrome(num)

        case 4:
            check_armstrong(num)

        case 5:
            reverse_number(num)

        case 6:
            sum_of_digits(num)

        case 7:
            print("Exited")
            break

        case _:
            print("Invalid choice")
