# Dice throw probability
try:
    number = int(input("Enter a number between 1 and 6: "))
    if 1 <= number <= 6:
        print("Probability is 1/6 = 0.1667")
    else:
        print("Number must be between 1 and 6")
except ValueError:
    print("Please enter a valid number")
