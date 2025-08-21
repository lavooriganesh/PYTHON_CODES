a = int(input("Enter a number: "))
fact = 1
i = 1

while fact < a:
    i += 1
    fact = fact * i  # This line must be inside the loop

if fact == a:
    print(a, "is a factorial number")
else:
    print(a, "is not a factorial number")

