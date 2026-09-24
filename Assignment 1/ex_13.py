

numbers = {10, 20, 30, 40, 50}

print("Original Set:", numbers)

numbers.add(60)
print("After add:", numbers)

numbers.update([70, 80, 90])
print("After update:", numbers)

numbers.remove(20)
print("After remove:", numbers)

numbers.discard(30)
print("After discard:", numbers)

removed = numbers.pop()
print("Popped Element:", removed)
print("After pop:", numbers)


print("Length of set:", len(numbers))

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("\nSet 1:", set1)
print("Set 2:", set2)

print("Union:", set1.union(set2))

print("Intersection:", set1.intersection(set2))

print("Difference:", set1.difference(set2))

print("Symmetric Difference:",
      set1.symmetric_difference(set2))

subset = {1, 2, 3}

if subset.issubset(set1):
    print("Subset:", subset, "is a subset of Set 1")
else:
    print("Not a subset")

if set1.issuperset(subset):
    print("Set 1 is a superset of", subset)
else:
    print("Set 1 is not a superset")



set1.clear()
print("After clear:", set1)
