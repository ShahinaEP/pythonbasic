# Create a Set:
# Duplicate values will be ignored:
# True and 1 is considered the same value:
thisSet = {"apple", "banana", "cherry", "apple", True, False, 1, 2}
print(thisSet)
print(len(thisSet))

# Using the set() constructor to make a set:
constructor = set(("apple", "banana", "cherry")) # note the double round-brackets
print(constructor)

print('\n')
# Python - Access Set Items
for x in thisSet:
  print(x)

# Check if "banana" is present in the  set:
print(f"Check if banana is present in the set: {'banana' in thisSet}")

print('\n')
# Python - Add Set Items
thisSet.add("orange")
print(f'Add Set Items: {thisSet}')

# Add elements from tropical into thisset:
tropical = {"pineapple", "mango", "papaya"}
thisSet.update(tropical)
print(f'Add elements from tropical: {thisSet}')

mylist = ["kiwi", "orange"]
mylist2 = ("kiwi1", "orange1")
thisSet.update(mylist)
thisSet.update(mylist2)
print(f'Add elements from thisSet: {thisSet}')

# Python - Remove Set Items
thisSet.remove("apple")
print(f'Remove element from thisSet: {thisSet}')

# Python - Discard Set Items
thisSet.discard("orange1")
print(f'Discard element from thisSet: {thisSet}')

# Remove a random item by using the pop() method:
# x = thisSet.pop()
#
# print(x)
# print(f'Remove a random item by using the pop() method: {thisSet}')

# The del keyword will delete the set completely:
# thisSet.clear()
# print(x)
# print(f'Remove a random item by using the clear() method: {thisSet}')

print('\n')
# Python - Loop Sets
# You can loop through the set items by using a for loop:
print('You can loop through the set items by using a for loop:')
# for a in thisSet:
#     print(a)


print('\n')

# The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(f"The union() method returns a new set with all items from both sets: {set1.union(set2)}")
print(f"The update() method returns a new set with all items from both sets: {set1}")


# Keep the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
# Keep the items that are not present in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

# True and 1 is considered the same value:

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z)