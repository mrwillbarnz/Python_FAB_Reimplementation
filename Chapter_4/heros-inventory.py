# Hero's Inventory
# Demonstrates tuple creation

# Creating an empty tuple

inventory = ()

if not inventory:
    print("You are empty-handed.")

input("\nPress the enter key to continue.")

# Print a tuple
print("\nThe tuple inventory is:\n", inventory)

# Print each element in the tuple
print("\nYour items:")
for item in inventory:
    print(item)
input("\n\nPress the enter key to exit.")