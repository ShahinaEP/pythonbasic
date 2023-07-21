fruits = ("apple", "banana", "cherry", "banana")
# numbers = list()
square = [x**2 for x in range(len(fruits))]
print(f"square value :{tuple(square)}")
print('\n')
# Iterate through the items and print the values:
for a in fruits :
    print(a)
print('\n')
# Print all items by referring to their index number:
print("Print all items by referring to their index number:")
for a in range(len(fruits)):
    print(fruits[a])

print('\n')
i = 0
while i < len(fruits):
    print(fruits[i])
    i +=1

print('\n')

# Join Two Tuples
print("Join Two Tuples")
tuple1 = ("a", "b", "c", True, False)
tuple2 = (1, 2, 3)

print(f"Join Two Tuples: {tuple1 + tuple2}")

# Multiply Tuples
print(f"Multiply Tuples : {5*tuple1}")

# count
print(f"Count Tuples : {5*tuple1.count('a')}")

# index
print(f"Index Tuples : {5*tuple1.index('a')}")
