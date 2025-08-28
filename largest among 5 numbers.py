
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
e = int(input("Enter fifth number: "))


largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c
if d > largest:
    largest = d
if e > largest:
    largest = e

print("The largest number is:", largest)
