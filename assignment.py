# ex-1: Find GPA
bangla = int(input('Enter the bangla number:'))

if 79 < bangla < 101:
    print(f"Your number is {bangla}: A+")
elif 69 < bangla < 80:
    print(f"Your number is {bangla}: A")
elif 59 < bangla < 70:
    print(f"Your number is {bangla}: A-")
elif 49 < bangla < 60:
    print(f"Your number is {bangla}: B")
elif 39 < bangla < 50:
    print(f"Your number is {bangla}: C")
elif 32 < bangla < 40:
    print(f"Your number is {bangla}: D")
elif 0 <= bangla < 32:
    print(f"Your number is {bangla}: Fail")
else:
    print(f"Your number is {bangla}: Number is Invalid")

print('\n')


# ex-2: Find odd or even number
number = int(input('Enter your number:'))
if number % 2 == 1:
    print(f'Your enter number {number} is odd')
else:
    print(f'Your enter number {number} is even')

