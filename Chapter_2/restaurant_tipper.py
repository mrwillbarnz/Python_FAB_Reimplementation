# Restaurant Tipper
# Tips restaurants by calculating tips as a
# percentage of the bill, either 15 or 20%

print("Now your meal has come to and end, it's time to tip!")
tip = int(input("How much was your original meal (nearest pound please): "))
tip_one = tip * 0.15 * 100
tip_two = tip * 0.20 * 100
print("Here\'s how much you should tip at 15%: tip_one")
print("Here\'s how much you should tip @ 20%: tip_two")
