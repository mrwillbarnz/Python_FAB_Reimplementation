# Mood Computer
# Demonstrates the if-elif-else structure

import random

print ("I sense your energy. Your true emotions are coming across my screen.")
print ("You are...")

mood = random.randrange(3)

if mood == 0:
    # happy
    print \
        """
        
        
        
              """
elif mood == 1:
    # neutral
    print \
        """
        
        
        
              """
elif mood == 2:
    # sad
    print \
        """
        
        
        
              """
else:
    print("Illegal mood value! (You must be in a really bad mood).")

print("...today")

input("\n\nPress the enter key to exit.")