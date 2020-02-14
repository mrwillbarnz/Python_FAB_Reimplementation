# Hero's Inventory 2.0
# Demonstrates tuples

# Create a tuple with some items and display with a for loop
inventory = ("sword",
             "armour",
             "shield",
             "healing potion" )
print("Your items: ")
for item in inventory:
    print(item)

input("\nPress the enter key to continue.")

# Get the length of a tuple
print("You have, ", len(inventory), "items in your possession")

input("\nPress the enter key to continue.")

# Test for membership with in
if "healing potion" in inventory:
    print("You will live to fight another day.")

# Display one item through an index
index = int(input("\nEnter the index number for an item in inventory: "))
print("At index", index, "is", inventory[index])

# Display a slice
begin = int(input("\nEnter the index number to being a slice: "))
end = int(input("Enter the index number to end the slice: "))
print("inventory[", begin, ":", end, "]\t\t",
print("inventory[begin:end]"))

input("\nPress the enter key to continue.")

# Concatenate two tuples
chest = ("gold", "gems")
print("You find a chest. It contains:")
print(chest)
print("You add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory)
input("\n\nPress the enter key to exit.")