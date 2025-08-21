# Input two vectors
a = list(map(int, input("Enter Vector A: ").split()))
b = list(map(int, input("Enter Vector B: ").split()))

# Check same size
if len(a) != len(b):
    print("Vectors must be the same length")
else:
    # Addition
    add = [a[i] + b[i] for i in range(len(a))]

    # Subtraction
    sub = [a[i] - b[i] for i in range(len(a))]

    # Dot product
    dot = sum(a[i] * b[i] for i in range(len(a)))

    # Output
    print("Addition:", add)
    print("Subtraction:", sub)
    print("Dot Product:", dot)
