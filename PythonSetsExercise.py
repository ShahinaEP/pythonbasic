# 1.Check if "apple" is present in the fruits set.
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

# 2.Use the add method to add "orange" to the fruits set.
fruits.add("orange")
print(f'.Use the add method to add "orange" to the fruits set: {fruits}')


# 3.Use the correct method to add multiple items (more_fruits) to the fruits set.
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(f'Use the correct method to add multiple items (more_fruits) to the fruits set: {fruits}')

# 4.Use the remove method to remove "banana" from the fruits set.
fruits.remove("banana")
print(f'Use the remove method to remove "banana" from the fruits set: {fruits}')

# 5.Use the discard method to remove "banana" from the fruits set.
fruits.discard("banana")
print(f'Use the discard method to remove "banana" from the fruits set: {fruits}')
