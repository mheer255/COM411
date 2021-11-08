# ask user for number of bars
print("How many bars should be charged?")
charge = int(input())

# declare a control variable
charged = 0

# Display bars
print()

while charged < charge:
    charged = charged + 1
    print(f"Charging: {'█' * charged}")

print("The battery is fully charged.")
