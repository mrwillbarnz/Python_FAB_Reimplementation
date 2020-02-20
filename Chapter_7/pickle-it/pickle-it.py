# Pickle It
# Demonstrates pickling and shelving data
# Changed original cPickle module dependency to pickle for Python3
# cPickle is now no longer a module built into Python3, and
# it is easier to call pickle for all purposes of this script.

import pickle, shelve

print("Pickling lists.")
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz", "Vlassic"]
pickle_file = open("pickles1.dat", "w")
pickle.dump(variety, pickle_file)
pickle.dump(shape, pickle_file)
pickle.dump(brand, pickle_file)
pickle_file.close()

print("\nUnpickling lists.")
pickle_file = open("pickles1.dat", "r")
variety = pickle.load(pickle_file)
shape = pickle.load(pickle_file)
brand = pickle.load(pickle_file)

print(variety, "\n", shape, "\n", brand)
pickle_file.close()

print("\nShelving lists.")
pickles = shelve.open("pickles2.dat")

pickles["variety"] = ["sweet", "hot", "dill"]
pickles["shape"] = ["whole", "spear", "chip"]
pickles["brand"] = ["Claussen", "Heinz", "Vlassic"]

pickles.sync()

print("\nRetrieving the lists from a shelves file:")
for key in pickles.keys():
    print(key, "-", pickles[key])

input("\n\nPress the enter key to exit.")