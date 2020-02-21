# Property Critter
# Demonstrates get and set methods and properties

class Critter(object):
    """A virtual pet"""
    def __init__(self, name):
        print("A new critter has been born!")
        self.__name = name

    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        if new_name == "":
            print("A critter's name can't be the empty string.")
        else:
            self.__name = new_name
            print("Name change successful.")

# main
crit = Critter("Poochie")
crit.talk()

print("\nMy critter's name is:", print(crit.name))
crit.name = ""
print("\nAttempting to change my critter's name again.")
crit.name = "Randolph"

crit.talk()

input("\n\nPress the enter key to exit.")