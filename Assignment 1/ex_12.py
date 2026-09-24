
numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)


numbers.append(60)
print("After append:", numbers)

numbers.insert(2, 25)
print("After insert:", numbers)

numbers.extend([70, 80])
print("After extend:", numbers)


numbers.remove(25)
print("After remove:", numbers)

numbers.pop()
print("After pop:", numbers)

print("Length of list:", len(numbers))


numbers.append(30)
print("Count of 30:", numbers.count(30))

print("Index of 30:", numbers.index(30))

numbers.sort()
print("After sorting:", numbers)

numbers.reverse()
print("After reversing:", numbers)


print("Sliced List:", numbers[1:4])


numbers.clear()
print("After clear:", numbers)