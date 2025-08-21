# Input for Matrix A
print("Enter values for Matrix A:")
a11 = int(input("A[0][0]: "))
a12 = int(input("A[0][1]: "))
a21 = int(input("A[1][0]: "))
a22 = int(input("A[1][1]: "))

# Input for Matrix B
print("Enter values for Matrix B:")
b11 = int(input("B[0][0]: "))
b12 = int(input("B[0][1]: "))
b21 = int(input("B[1][0]: "))
b22 = int(input("B[1][1]: "))

# Addition
add = a11 + b11
add = a12 + b12
add = a21 + b21
add = a22 + b22

# Subtraction
sub = a11 - b11
sub = a12 - b12
sub = a21 - b21
sub = a22 - b22

# Multiplication (Matrix A × Matrix B)
mul = a11*b11 + a12*b21
mul = a11*b12 + a12*b22
mul = a21*b11 + a22*b21
mul = a21*b12 + a22*b22

# Output
print("\n Result of A + B:")
print(f"[{add} {add}]")
print(f"[{add} {add}]")

print("\n Result of A - B:")
print(f"[{sub} {sub}]")
print(f"[{sub} {sub}]")

print(f"\n Result of A * B:")
print(f"[{mul} {mul}]")
print(f"[{mul} {mul}]")
