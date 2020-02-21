# Critter Caretaker
# A virtual pet to care for

class Critter(object):
    """A virtual pet."""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
    def __get_mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            mood = "happy"
        elif 5 <= unhappiness <= 10:
            mood = "okay"
        elif 11 <= unhappiness <= 15:
            mood = "frustrated"
        else:
            mood = "mad"
        return mood
    mood = property(__get_mood)

    def talk(self):
        print ("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()
    def eat(self, food = 4):
        print("Bruppp. Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
    def play(self, fun = 4):
        print("Whee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def main():
        crit_name = input("What do you want to name your critter?: ")
        crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print( \
            """
            Critter Caretaker

            0 - Quit
            1 - Listen to your critter.
            2 - Feed your critter.
            3 - Play with your critter.
            """
    choice = input("Choice: ")
    print

    # exit
    if choice == "0":
        print("Good-bye.")
    # listen to your critter
    elif choice == "1":
        crit.talk()
    # feed your critter
    elif choice == "3":
        crit.play()
    # some unknown choice
    else:
        print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.")



# TODO
# 1. Improve the Critter Caretaker program by allowing the user to specify how much food he or she feeds the critter and how long
# he or she plays with the critter. Have these values affect how quickly the critter's hunger and boredom levels drop.
#
# 2. Write a program that simulates a television by creating it as an object. The user should be able to enter a channel number and raise or lower
# the volume. Make sure that the channel number and volume level stay within valid ranges.
#
# 3. Create a "back door" in the Critter Caretaker program, that shows the exact values of the object's attributes. Accomplish this by
# printing the object when a secret selection, not listed in the menu, is entered as the user's choice. (Hint: Add the special method __str__() to the Critter Class.)
#
# 4. Create a Critter Farm program by instantiating several Critter objects and keeping track of them through a list.
# Mimic the Critter Caretaker program, but instead of requiring the user to care for a single critter, require him or her to care for an entire farm.
# Each menu choice should allow the user to perform some action for all of the critters (feed all of the critters, play with all of the critters, or listen to all of the critters).
# To make the program interesting, give each critter random starting hunger and boredom levels.

