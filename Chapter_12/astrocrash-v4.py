# Astrocrash04
# Addition of the Missile Class, and defining the class trigger
# (when to fire the missile)!

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
# The Missile Class
class Missile(games.Sprite):
    """ A missile launched by the player's ship. """
    image = games.load_image("missile.bmp")
    sound = games.load_sound("missile.wav")
    BUFFER = 40
    VELOCITY_FACTOR = 7
    LIFETIME = 40
    def __init__(self, ship_x, ship_y, ship_angle):
        """ Initialize the missile sprite. """
        Missile.sound.play()
        # convert to radians
        angle = ship_angle * math.pi / 180

        # calculate missile's starting position
        buffer_x = Missile.BUFFER * math.sin(angle)
        buffer_y = Missile.BUFFER * -math.cos(angle)
        x = ship_x + buffer_x
        y = ship_y + buffer_y

        # calculate missile's velocity components
        dx = Missile.VELOCITY_FACTOR * math.sin(angle)
        dy = Missile.VELOCITY_FACTOR * -math.cos(angle)

        # create the missile
        super(Missile, self).__init__(image = Missile.image,
        x = x, y = y, dx = dx, dy = dy)

        self.lifetime = Missile.LIFETIME

        def update(self):
            """ Move the missile. """
            # if lifetime is up, destroy the missile
            self.lifetime -= 1
            if self.lifetime == 0:
                self.destroy()
            # wrap the missile screen around
            if self.top > games.screen.height:
                self.bottom = 0
            if self.bottom < 0:
                self.top = games.screen.height
            if self.left > games.screen.width:
                self.right = 0
            if self.right < 0:
                self.left = games.screen.width

# kick it off!
main()