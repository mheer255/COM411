# Ask user for the direction
print("Please enter the first number.")
first_number = input()

print("Please enter the second number.")
second_number = input()

# Determine which message to display
if first_number < second_number:
    print("The first number is the smallest.")
elif first_number > second_number:
    print("The second number is the smallest.")
else:
    print("The two numbers are equal.")