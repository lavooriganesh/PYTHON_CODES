n = int(input("Enter how many terms: "))

first = 0
second = 1

print("Fibonacci sequence:")

for i in range(n):
    print(first, end=" ")     
    next_num = first + second 
    first = second           
    second = next_num
