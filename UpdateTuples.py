x = ("apple", "banana", "cherry")
# Change Tuple Values
y = list(x)
y[1] = "kiwi"

# add tuple:
y.append("orange")
x = tuple(y)
x += tuple(y)
print(x)
print(y)

# Convert the tuple into a list, remove item and convert it back into a tuple:
z = list(x)
z.remove('kiwi')

# delete the tuple completely:
del z[-1]
x = tuple(z)
print(x)
