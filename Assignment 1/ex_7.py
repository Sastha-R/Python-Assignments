num = int(input("Enter a number: "))

original = num

# Number of digits
temp = str(num)
count = len(temp)


# Sum and Product of digits
temp = num
digit_sum = 0
digit_product = 1

while temp > 0:
    digit = temp % 10

    digit_sum += digit
    digit_product *= digit

    temp //= 10

# Reverse
temp = str(num)

reverse = int(temp[::-1])

print(reverse)


# Even or Odd
even_odd = "Even" if num % 2 == 0 else "Odd"

# Prime or Not Prime
if num < 2:
    prime = False
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

# Palindrome
if original == reverse:
    palindrome = "Palindrome"
else:
    palindrome = "Not Palindrome"

# Armstrong
temp = num
armstrong_sum = 0

while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** count
    temp //= 10

if armstrong_sum == original:
    armstrong = "Armstrong"
else:
    armstrong = "Not Armstrong"


# Display results
print("\n----- Number Analysis -----")
print("Number of digits :", count)
print("Sum of digits    :", digit_sum)
print("Product of digits:", digit_product)
print("Reverse          :", reverse)
print("Even/Odd          :", even_odd)
print("Prime/Not Prime   :", "Prime" if prime else "Not Prime")
print("Palindrome        :", palindrome)
print("Armstrong         :", armstrong)