# Astrocrash03
# Adds the Velocity_STEP variable
# Adds sound queues.
# Adds wrapping so the ship can't go out-of-bounds

import random
import livewires import games
import math


games.init(screen_width = 640, screen_height = 480, fps = 50)

class Asteroid(games.Sprite):
    """ An asteroid which floats across the screen. """
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL: games.load_image("asteroid_small.bmp"),
              MEDIUM: games.load_image("asteroid_med.bmp"),
              LARGE: games.load_image("asteroid_big.bmp") }
    SPEED = 2

    def __init__(self, x, y, size):
        """ Initialize asteroid sprite. """
        super(Asteroid, self).__init__(
            image = Asteroid.images[size],
            x = x, y = y,
            dx = random.choice([1, -1]) * Asteroid.SPEED * random.random()/size,
            dy = random.choice([1, -1]) * Asteroid.SPEED * radom.random()/size)
        self.size = size

    def update(self):
        """ Wrap around screen. """
        if self.top > games.screen.height:
            self.bottom = 0

        if self.bottom < 0:
            self.top = games.screen.height

        if self.left > games.screen.height
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width

    def main():
        # establish background
        nebula_image = games.load_image("nebula.jpg")
        games.screen.background = nebula_image

        # create 8 asteroids
        for i in range(8):
            x = random.randrange(games.screen.width)
            y = random.randrange(games.screen.height)
            size = random.choice([Asteroid.SMALL, Asteroid.MEDIUM, Asteroid.LARGE])
            new_asteroid = Asteroid(x = x, y = y, size = size)
            games.screen.add(new_asteroid)

class Ship(games.Sprite):
    """ The player's ship. """
    image = games.load_image("ship.bmp")
    VELOCITY_STEP = .03
    ROTATION_STEP = 3
    sound = games.load.sound("thrust.wav")
    # apply thrust based on up arrow key
    # Add SFX queue whenever key pressed
    if games.keyboard.is_pressed(games.K_UP):
        Ship.sound.play()
    # change velocity components based on ship's angle
    angle = self.angle * math.pi / 180 # convert to radians
    # sin and cos of velocity for angular movement
    self.dx += Ship.VELOCITY_STEP * math.sin(angle)
    self.dy += Ship.VELOCITY_STEP * -math.cos(angle)
    def update(self):
        """ Rotate based on keys pressed. """
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP
        # wrap the ship around screen
        if self.top > games.screen.height:
            self.bottom = 0
        if self.bottom < 0:
            self.top = games.screen.height
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
    # create the ship
    the_ship = Ship(image = Ship(image = Ship.image,
    x = games.screen.width/2
    y = games.screen.height/2)
    games.screen.add(the_ship))


# Sound Classes
# kick it off!
main()