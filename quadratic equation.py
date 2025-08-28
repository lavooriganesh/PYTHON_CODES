# Program to display a quadratic equation using user input

# User gives values
a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))
d = int(input("Enter constant d:"))

# Display equation
print("Quadratic Equation is:")
print(f"{a}x^2 + {b}x + {c} = 0")
print(f"{a}x^3 + {b}x^2 + {c}x + {d}")
