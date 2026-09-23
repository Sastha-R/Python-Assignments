customer_name = input("Enter customer name: ")
units = float(input("Enter units consumed: "))

if units < 0:
    print("Invalid units")
else:
    if units <= 100:
        charge = units * 2

    elif units <= 200:
        charge = (100 * 2) + ((units - 100) * 3)

    elif units <= 400:
        charge = (100 * 2) + (100 * 3) + ((units - 200) * 5)

    else:
        charge = (100 * 2) + (100 * 3) + (200 * 5) + ((units - 400) * 7)

    tax = charge * 0.05

    total_bill = charge + tax

    print("Customer Name: ", customer_name)
    print("Units Consumed: ", units)
    print(" Charge: ", charge)
    print("Tax: ", tax)
    print("Total Bill: ", total_bill)