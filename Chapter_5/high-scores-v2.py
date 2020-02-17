# High Scores 2.0
# Demonstrates nested sequences

scores = []
choice = None

while choice != "0":
    print (\
        """
        High Scores Keeper

        0 - Quit
        1 - List Scores
        2 - Add a Score
        """)

choice = input("Choice: ")
print( \
    if choice == "0":
        print("Good-bye.")
    elif choice == "1":
        print("NAME\tSCORE")
            for entry in scores:
                score, name = entry
                print(name, "\t", score)
            elif choice == "2":
                name = input("What is the player's name?: ")
                score = int(input("What score did the player get?: "))
                entry = (score, name)
                scores.append(entry)
                scores.sort()
                scores.reverse()
                scores = scores[:5] )
