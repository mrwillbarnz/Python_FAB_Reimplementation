# Losing Battle
# Demonstrates the dreaful infinite loop
# You'll have to force-close this program by pressing Ctrl+C to force-stop it!

# Pre-amble
print("Your lone hero is surrounded by a massive army of trolls.")
print("Their decaying green bodies stretch out, melting into the horizon.")
print("Your hero unsheathes his sword and begins the last fight of hise life.\n")

# Define health, troll and damage variables
health = 10
trolls = 0
damage = 3

# Health Vs Damage vs trolls
while health != 0:
    trolls += 1
    health = health - damage

    print("Your hero swings and defeats an evil troll, " 
    "but takes", damage, "damage points.\n")

# Closing statement
print("Your hero fought valiantly and defeated", trolls, "trolls.")
print("But alas, your hero is no more.")

# Exit program! (Lol you can't)
input("\n\nPress the enter key to exit.")