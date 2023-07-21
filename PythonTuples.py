
# Access Tuple Items
mytuple = ("apple", "banana", "cherry")
print(mytuple)
# Print the second item in the tuple:
print(mytuple[0])


# Negative Indexing
print(mytuple[-1])

# Tuples allow duplicate values:

# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)

# Return the third, fourth, and fifth item:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# This example returns the items from the beginning to, but NOT included, "kiwi":
print(thistuple[:4])

# This example returns the items from "cherry" and to the end:
print(thistuple[2:])


# This example returns the items from index -4 (included) to index -1 (excluded)
print(thistuple[-4:-1])

# Check if "apple" is present in the tuple:
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

