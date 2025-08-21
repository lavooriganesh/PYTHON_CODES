
print("Enter elements of Vector A one by one:")
a1 = int(input("A[0]: "))
a2 = int(input("A[1]: "))
a3 = int(input("A[2]: "))

print("Enter elements of Vector B one by one:")
b1 = int(input("B[0]: "))
b2 = int(input("B[1]: "))
b3 = int(input("B[2]: "))

add1 = a1 + b1
add2 = a2 + b2
add3 = a3 + b3

sub1 = a1 - b1
sub2 = a2 - b2
sub3 = a3 - b3

scalar = int(input("Enter a scalar to multiply Vector A: "))
mul1 = a1 * scalar
mul2 = a2 * scalar
mul3 = a3 * scalar

print("\nVector A + Vector B =")
print(f"{add1}")
print(f"{add2}")
print(f"{add3}")

print("\nVector A - Vector B =")
print(f"{sub1}")
print(f"{sub2}")
print(f"{sub3}")

print(f"\nVector A * {scalar} =")
print(f"{mul1}")
print(f"{mul2}")
print(f"{mul3}")
