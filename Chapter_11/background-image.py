# Background Image
# Demonstrates setting the background image of a graphics screen

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

wall_image = games.load_image("wall.jpg", transparent = False)
games.screen_background = wall_image

# initiate the mainloop
games.screen.mainloop()

