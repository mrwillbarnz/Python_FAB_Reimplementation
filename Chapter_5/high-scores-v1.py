# High Scores v1
# Demonstrates list methods

scores = []
choice = None

while choice != "0":
    print (\
        """
        High Scores Keeper
        0 - Exit
        1 - Show Scores
        2 - Add a Score
        3 - Delete a Score
        4 - Sort Scores
        """ )
choice = input("Choice: ")
print(
    if choice == "0":
        print("Good-bye.")
    elif choice == "1":
        print("High Scores"
        for score in scores:
            print(score))
    elif choice == "2":
        score = int(input("What score did you get?: ")))
        scores.append(score)
    elif choice: == "3":
        score = int(input("Delete which score?: "))
        if score in scores:
            scores.remove(score)
        else:
            print(score, "isn't in the high scores list.")
    elif choice == "4":
        scores.sort()
        scores.reverse()
        else:
            print("Sorry, but", choice, "isn't a valid choice.")
input("\n\nPress the enter key to exit.")


