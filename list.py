li = ["abc", 34, True, 40, "male",{"name":"pia", "id":1234}]
print(len(li))

# Change Item Value
li[5]['name'] = "Shahina"
print(li[5]['name'])
print(li)

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
# This example returns the items from the beginning to
print(thislist[:2])
# This example returns the items from "cherry" to the end:
print(thislist[1:])
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

thislist1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist1[-4:-1])

# Check if Item Exists
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

else:
    print("No, 'apple' is in the fruits list")

# Change a Range of Item Values
thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist3[1:2] = ["blackcurrant", "watermelon"]
thislist3.insert(4, "watermelon")
thislist3.append("orange")
thislist3.insert(0, "orange")
tropical = ["mango", "pineapple", "papaya"]
thislist3.extend(tropical)
print(thislist3)


# Python - Remove List Items
thislist3.remove("kiwi")
thislist3.pop(0)
del thislist3[0]
# del thislist3
# thislist3.clear()
print(thislist3)

