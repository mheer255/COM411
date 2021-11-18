# ask user to enter name, age, weight, and height
print("what is your name ?")
name = input()
print("How old are you (in years)?")
age = int(input())
print("What is your weight?")
weight = float(input())

print("What is your height?")
height = float(input())

# Calculate bmi
bmi = weight / (height ** 2)

# Display result
print(f"{name} your bmi is {bmi}")

