emp_name = input("Enter your name: ")

basic_salary = float(input("Enter basic salary: "))

experience = int(input("Enter years of experience: "))

hra = 0.2 * basic_salary    
da = 0.1 * basic_salary
gross_salary = basic_salary + hra + da

if experience < 2:
    bonus = 1000
elif experience <= 5:
    bonus = basic_salary * 0.05
elif experience <= 10:
    bonus = basic_salary * 0.1
else:
    bonus = basic_salary * 0.15

net_salary = gross_salary + bonus

print("Employee Name: ", emp_name)
print("Basic Salary: ", basic_salary)
print("Gross Salary: ", gross_salary)
print("Bonus: ", bonus)
print("Net Salary: ", net_salary)
print("Salary Category: ", "Low" if net_salary < 50000 else "Medium" if net_salary < 100000 else "High")