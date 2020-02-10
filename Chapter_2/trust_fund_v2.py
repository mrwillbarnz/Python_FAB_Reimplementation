# Trust Fund Buddy v2 (Good)
# Demonstrates type conversion

print ( \
    """
         Trust Fund Buddy

Totals your monthly spending so that your trust fund doesn't run out
(and you're forced to get a real job).

Please enter the requested, monthly costs. Since you're rich, ignore pennies
and only use dollar amounts.
    """)

car = int(input("Lamborghini tune-ups: "))
rent = int(input("Manhattan Apartment: "))
jet = int(input("Private Jet Rental: "))
gifts = int(input("Gifts: "))
food = int(input("Dining Out: "))
staff = int(input("Staff (butlers, chef, drivers, assistant): "))
guru = int(input("Personal Guru and Coach: "))
games = int(input("Computer Games: "))

total = car + rent + jet + gifts + food + staff + guru + games

print("\n Grand Total: ", total)

input("\n\nPress the enter key to exit.")

