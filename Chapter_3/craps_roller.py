# Craps Roller
# Demonstrates random number generation

import random
# Generate random numbers 1-6
die1 = random.randrange(6) + 1
die2 = random.randrange(6) + 1

total = die1 + die2

print("You rolled a", die1, "and a", die2, "for a total of", total)