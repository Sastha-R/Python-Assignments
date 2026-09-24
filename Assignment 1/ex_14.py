

student = {
    "name": "saul",
    "age": 21,
    "course": "BCA",
    "mark": 85
}

print("Original Dictionary:", student)


print("Course:", student.get("course"))


student["city"] = "Coimbatore"
print("After adding:", student)

student["mark"] = 90
print("After updating mark:", student)

student.update({"age": 22, "course": "Computer Applications"})
print("After update():", student)


print("Keys:", student.keys())

print("Values:", student.values())

print("Items:", student.items())

student.pop("city")
print("After pop():", student)

student.popitem()
print("After popitem():", student)


print("Length:", len(student))

print("\nKeys:")
for key in student:
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKey-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)


student.clear()
print("After clear:", student)
