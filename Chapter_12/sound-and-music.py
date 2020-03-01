# Sound-and-Music
# Demonstrates playing sound and music files

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

# load a sound file
missile_sound = games.load_sound("missile.wav")

# load the music file
games.music.load("theme.mid")

# Menu system
choice = None
while choice != "0":
    print( \
        """
        Sound and Music

        0 - Quit
        1 - Play Missile Sound
        2 - Loop Missile Sound
        3 - Stop Missile Sound
        4 - Play Theme Music
        5 - Loop theme music
        6 - Stop theme music
        """

        choice = input("Choice: ")
        print()
    # exit
    if choice == "0":
        print("Good-bye.")

    # Play Missile Sound
    elif choice == "1":
        missle_sound.play()
        print("Play missile sound.")
    # loop missile sound
    elif choice == "2":
        loop = int(input("Loop how many extra times? (-1 = forever): "))
        missile_sound.play(loop)
        print("Looping missile sound.")
    # stop missile sound
    elif choice == "3":
        missile_sound.stop()
        print("Printing missile sound.")

    # Play theme music
    elif choice == "4":
        games.music.play()
        print("Playing theme music.")
    # loop theme music
    elif choice == "5":
        loop = int(input("Loop how many extra times? (-1 = forever): "))
        games.music.play(loop)
        print("Looping theme music.")
    # stop theme music
    elif choice == "6":
        games.music.stop()
        print("Stopping theme music.")
    # some unknown choice
    else:
        print("\nSorry, but", choice, "isn't a valid choice.")
input("\n\nPres the enter key to exit.")
