# Car Salesman
# User enters a base price of a car
# Extra fees are added on
# Tax and License are added as a percentage of the base-price
# Displays total cost with extras

# Variable Definitions
car = input("How much is your car?(Whole amount please): ")
tax = car * 0.20 * 100
dlicense = int(car * 0.15 * 100)
dealerprep = 1000
destination_charge = 1000



print("Time to buy your new car")
print("Have you considered the costs?")
input("Here's your bill:")