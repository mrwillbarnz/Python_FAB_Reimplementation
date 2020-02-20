# Handle-it
# Demonstrates handling exceptions

# try/except
try:
    num = float(input("Enter a number: "))
except:
    print("Something's wrong!")

# specifying exception type
try:
    num = float(input("\nEnter a number: "))
except(ValueError):
    print("That wasn't a number!")

# handle multiple exceptions
print(
for value in (None, "Hi!"):
        try:
            print("Attempting to convert", value, "->",
            print float(value))
    except(TypeError, ValueError):
        print("Something went wrong!"))

print(
    for value in (None, "Hi!"):
        try:
            print("Attempting to convert", value, "-->",
            print float(value))
        except(TypeError):
            print("I can only convert a string or a number!")
        except(ValueError):
            print("I can only convert a string of digits!"))

# get an exception's argument
try:
    num = float(input("\nEnter a number: ")
except(ValueError), e:
    print("That wasn't a number! Or as Python would say:\n", e))


# try/except/else
try:
    num = float(input("\nEnter a number: ")
except(ValueError):
    print("That wasn't a number!")
else:
    print("You entered a number!", num))

input("\n\nPress the enter key to exit.")