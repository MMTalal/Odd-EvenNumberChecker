# Odd and Even Number Checker
# This program checks if a given number is positive, negative, odd, or even

# Prompt the user to enter a number
print("Odd and Even No. checker")
print("We can check your number if it is positive or negative, odd or even")
number = float(input("Please input your number here? "))

# Check if the number is zero
if number == 0:
    print("Your number is not even or odd, your number is ZERO. Please try again and input another number.")

# Check if the number is positive
elif number > 0:
    print("Your number is positive.")
    # Check if the positive number is even or odd
    if number % 2 == 0:
        print("Your number is even.")
    else:
        print("Your number is odd.")

# Check if the number is negative
else:
    print("Your number is negative.")
    # Check if the negative number is even or odd
    if number % 2 == 0:
        print("Your number is even.")
    else:
        print("Your number is odd.")