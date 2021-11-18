# ask user for the type of adventure
print("what type of adventure is it?")
adventure_type = input()
# determine what message to display
if (adventure_type == "scary") or (adventure_type == "short"):
    print("entering the dark forest!")
elif (adventure_type == "safe") or (adventure_type == "long"):
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")
