# Trivia Challenge
# Demonstrates Files and Exceptions
# Trivia game that reads a plain-text file.
#
# TODO
# 1. Improve the Trivia Challenge game so that each question has a unique
# point value associated with it. The player's score
# should be the total of all the point values of the questions
# he or she answers correctly.
# 2. Improve the Trivia Challenge game so that it maintains a high-scores
# list in a file. The program should record the player's name and score
# if the player makes the list.
# Store the high scores using a pickled object.
# 3. Change the way the high-scores functionality you create in
# the last challenge is implemented. This time, use a plain-text
# file to store the list.
# 4. Create a trivia game that tests the player's knowledge
# of Python files and exceptions

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except(IOError), e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)

    return category, question, answers, correct, explanation

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to the Trivia Challenge!\n")
    print("\t\t", title, "\n")

def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

# get first block

category, question, answers, correct, explanation = next_block(trivia_file)
while category:
    # ask a question
    print(category)
    print(question)
    for i in range(4):
        print("\t", i + 1, "-", answers[i])

# get answer
answer = input("What's your answer?: ")

# check answer
if answer == correct:
    print("\nRight!"),
    score += 1
else:
    print("\nWrong!."),
    print(explanation)
    print("Score:", score, "\n\n")

# get next block
category, question, answers, correct, explanation = next_block(trivia_file)

trivia_file.close()

print("That was the last question!")
print("You're final score is:", score)

main()
input("\n\nPress the enter key to exit.")


