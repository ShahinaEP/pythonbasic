# Packing a tuple:
fruits = ("apple", "banana", "cherry", "banana")
print(fruits)

# Unpacking a tuple:
(apple, banana,*cia) = fruits
print(cia)


# Using Asterisk*
fruit = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruit

print(green)
print(yellow)
print(red)
