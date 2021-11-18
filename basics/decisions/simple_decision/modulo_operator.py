# ask user to enter a number
print("Please enter a whole number.")
number = int(input())
# Display relevant message
if number % 2 == 0:
    print(f"The number is an even number.")
else:
    print(f"The number is an odd number.")
