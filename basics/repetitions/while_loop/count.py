# ask user to avoid cables
print("how many live cables must i avoid?")
cables_to_avoid = int(input())

# declare a control variable
cables_avoided = 0

# avoid cables
print()
while cables_avoided < cables_to_avoid:
    print("Avoiding...", end="")
    cables_avoided = cables_avoided + 1
    print(f"Done! cables avoided.")


# display message
print("All live cables have been avoided.")


