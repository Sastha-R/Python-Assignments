no_of_products = int(input("Enter number of products: "))

subtotal = 0

for i in range(no_of_products):
    price = float(input(f"Enter price of product {i + 1}: "))
    subtotal += price

if subtotal < 1000:
    discount = 0
elif subtotal < 5000:
    discount = subtotal * 0.05
elif subtotal < 10000:
    discount = subtotal * 0.1
else:
    discount = subtotal * 0.15

discounted_amt = subtotal - discount

tax = discounted_amt * 0.05

final_amount = discounted_amt + tax

print("Subtotal: ", subtotal)
print("Discount: ", discount)
print("Tax: ", tax)
print("Final Amount: ", final_amount)