
# You can loop through the list items by using a for loop:
print("loop through the list items by using a for loop:")
thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

# Print all items by referring to their index number:
print("Print all items by referring to their index number:")
# for i in range(len(thislist)):
  # print(thislist[i])

# A shorthand for loop that will print all items in a list:
print("A short hand for loop that will print all items in a list:")
# [print(x) for x in thislist]

# Using a While Loop
print("Using a While Loop:")
i = 0
# while i < len(thislist):
#     # print(thislist[i])
#     i = i + 1
# List Comprehension

fruits = ["apple", "cherry","banana",  "kiwi", "mango"]
# newlist = []
# newlist = [x for x in fruits if "a" in x]
# for x in fruits:
#     # newlist.append(x)
#     if "a" in x:
#         newlist.append(x)
#
# print(newlist)
#
#
number = [4, 1, 3, 5, 7]
# squre = [x**2 for x in number]
# print(squre)

# Sort the list alphabetically:
# fruits.sort()
fruits.sort(reverse = True)
# fruits.sort(key = str.upper())
number.sort(reverse = True)
# print(fruits)
# print(number)

# Make a copy of a list with the copy() method:
mylist = fruits.copy()
mylist.sort()
# print(mylist)

# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)

for x in list1 :
    list2.append(x)

list1.extend(list2)
print(list1)
print(list2)

# count
# apple = fruits.count("banana")
apple = fruits.index("banana")
print(apple)


