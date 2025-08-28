# Take input from the user
var_name = input("Enter a variable name: ")

# Check if it's a valid identifier
if var_name.isidentifier():
    print("Valid variable name.")
else:
    print("Invalid variable name.")
