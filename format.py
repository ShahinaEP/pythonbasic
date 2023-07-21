n1 = 28
n2 = 50

userName = "Shahina"
Roll = "10"

print(f"My name is {userName} & my roll is {Roll}")
print(f"This is my super number {n1+n2}")


# Binary Types
list = [1, 3, 5, 34, 255]
b = bytes(list)

print(type(b))

# Binary Types byteArray
list1 = [1, 3, 5, 34, 255]
b1 = bytearray(list1)
print(type(b1))

print("Before Change", b1[0])

b1[0] = 100
print("After Change", b1[0])

# None Type
x = None

print(x)
print(type(x))


# Sequence Types
# List Type Data
li = ["apple", "banana", "cherry", 23, 17]
print(li)
print(type(li))
print("Before Change", li)

li[0] = 100
print("After Change", li)

# Tuple Type Data
tu = ("apple", "banana", "cherry", 23, 17)
print(tu)
print(type(tu))
# print("Before Change", tu)

# tu[0] = 100
# print("After Change", tu)

# Range Type Data
ra = range(6)
print(ra)
print(type(ra))
for i in ra:
    print(f"Range value :{i}")
