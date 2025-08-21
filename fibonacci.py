a = int(input("Enter how many Fibonacci numbers to print: "))

n = 0
m = 1

print("Fibonacci Series:")

for i in range(a):
    print(n, end=' ')
    next = n + m
    n = m
    m = next
