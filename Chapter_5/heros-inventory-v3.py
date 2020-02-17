# Hero's Inventory
# Demonstrates lists

# Create a list with some items and display with a for loop

inventory = ["sword", "armour", "shield", "healing potion"]
print("Your items:")
for item in inventory:
    print(item)
input("\nPress the enter key to continue.")

# Get the length of the list

print("You have", len(inventory), "items in your possession.")

input("\nPress the enter key to continue.")

# test for membership with in
if "healing potion" in inventory:
    print("You will live to fight another day.")

# Display a slice
begin = int(input("\nEnter the index number to begin a slice: "))
end = int(input("Enter the index number to end the slice: "))
print("inventory[", begin,":", end, "]\t\t")

print(inventory[begin:end])

input("\nPress the enter key to continue.")

# Concatenate two lists

chest = ["gold", "gems"]
print("You find a chest which contains:")
print(chest)
print("You add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory)

input("\nPress the enter key to continue.")

# assign by index
print("You trade your sword for a crossbow.")
inventory += chest
print("Your inventory is now: ")
print(inventory)
input("\nPress the enter key to continue.")

# assign by slice
print("You use your gold and gems to buy an orb of fortune telling.")
inventory[4:6] = ["orb of fortune telling"]
print("Your inventory is now:")
print(inventory)

# delete an element
print("In a great battle, your shield is destroyed.")
del inventory[2]
print("Your inventory is now:")
print(inventory)

input("\nPress the enter key to continue.")

# delete a slice
print("Your crossbow and armour are stolen by thieves.")
del(inventory[:2])
print("Your inventory is now:")
print(inventory)

input("\n\nPress the enter key to exit.")
del(inventory[:2])
