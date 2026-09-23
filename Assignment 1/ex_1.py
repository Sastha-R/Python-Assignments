Marks = []
subjects = ["Tamil","English","Maths","Science","Computer"]
std_name = input("Enter your name:")

for i in range(5):
    Mark = (int(input(f"Enter {subjects[i]} mark : ")))

    while(Mark < 0 or Mark > 100):
        Mark = int(input("invalid mark enter the mark again: "))

    Marks.append(Mark)


total = sum(Marks)

average = total / 5

if min(Marks) < 40:
    grade = "F"
elif average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"


print("Name : ",std_name)
print("Total : ",total)
print("Average : ",average)
print("Grade : ",grade)
print("Status : ","pass" if grade != "F" else "Fail")



