print("Choose an option:")
print("1. Coin Toss Probability")
print("2. Dice Throw Probability")

choice = input("Enter 1 or 2: ")

if choice == "1":
    outcome = input("Enter Heads or Tails: ").capitalize()
    if outcome in ["Heads", "Tails"]:
        print("Probability of getting", outcome, "is 0.5")
    else:
        print("Invalid coin outcome")

elif choice == "2":
    try:
        number = int(input("Enter a number between 1 and 6: "))
        if 1 <= number <= 6:
            print(f"Probability of getting {number} is 1/6 = {1/6:.4f}")
        else:
            print("Number must be between 1 and 6")
    except ValueError:
        print("Invalid number")

else:
    print("Invalid choice")
