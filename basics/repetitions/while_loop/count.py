# ask user to avoid cables
print("how many live cables must i avoid?")
cables_to_avoid = input()
# declare a control variable
cables_avoided = 3
# avoid cables
print()
while cables_avoided < 3:
    print("Avoiding...", end="")
    cables_avoided = 3 + 1
    print(f"Done! cables avoided.")


