# Astrocrash08
# Final Version
# Added the theme music, import Livewires, games, color module
# Added __init__() Method
# Added play(), advance(), end(), main() function.

# Import modules
import random
import livewires import games, color
import math

# Initialise the game window
games.init(screen_width = 640, screen_height = 480, fps = 50)

class Game(object):
    """ The game itself."""
    def __init__(self):
        """ Initialize Game object."""
        # set level
        self.level = 0

        # load sound for level advance
        self.sound = games.load_sound("level.wav")

        # create score
        self.score = games.Text(value = 0, size = 30, color = color.white, top = 5, right = games.screen.width - 10, is_collideable = False)
        games.screen.add(self.score)

        # create Player's ship
        self.ship = Ship(game = self, x = games.screen.width/2,
        y = games.screen.height/2)
        games.screen.add(self.ship)
    def play(self):
        """ Play the game. """
        # begin theme music
        games.music.load("theme.mid")
        games.music.play(-1)

        # load and set background
        nebula_image = games.load_image("nebula.jpg")
        games.screen.background = nebula_image

        # advance to level 1
        self.advance()

        # start play
        games.screen.mainloop()

    def advance(self):
        """ Advance to the next game level. """
        self.level += 1

    def main():
    astrocrash = Game()
    astrocrash.play()

# amount of space around ship to preserve when creating asteroids
BUFFER = 150

# create new asteroids
for i in range(self.level):
    # calculate an x and y at least BUFFER distance from the ship

    # choose minimum distance along x-axis and y-axis
    x_min = random.randrange(BUFFER)
    y_min = BUFFER - x_min

    # choose distance along x-axis based on minimum distance
    x_distance = random.randrange(x_min, games.screen.width - x_min)
    y_distance = random.randrange(y_min, games.screen.height - y_min)

    # calculate location based on distance
    x = self.ship.x + x_distance
    y = self.ship.y + y_distance

    # wrap around screen, if necessary
    x %= games.screen.width
    y %= games.screen.height

    # create the asteroid
    new_asteroid = Asteroid(game = self, x = x, y = y, size = Asteroid.LARGE)

    games.screen.add(new_asteroid)

    # display level number
    level_message = games.Message(value = "Level " + str(self.level),
    size = 40,
    color = color.yellow,
    x = games.screen.width/2
    y = games.screen.height/2
    lifetime = 3 * games.screen.fps,
    is_collideable = False)

    # play new level sound (except at first level)
    if self.level > 1:
        self.sound.play()
    def end(self):
        """ End the game. """
        # Show 'game over' for 5 seconds.
        end_message = games.Message(value = "Game Over",
        size = 90, color = color.red,
        x = games.screen.width/2,
        y = games.screen.height/2,
        lifetime = 5 * games.screen.fps,
        after_death = games.screen.quit,
        is_collideable = False)
        games.screen.add(end_message)

class Wrapper(games.Sprite):
    """ A Sprite that wraps around the screen. """
    def update(self):
        """ Wrap sprite around the screen."""
        if self.top > games.screen.height:
            self.bottom = 0
        if self.bottom < 0:
            self.top = games.screen.height
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
    def die(self):
        """ Destroy self."""
        self.destroy()

class Collider(Wrapper):
    """ A Wrapper that can collide with another object. """
    def update(self):
        """ Check for overlapping sprites."""
        super(Collider, self).update()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()
    def die(self):
        """ Destroy self and leave explosion behind. """
        new_explosion = Explosion(x = self.x, y = self.y)
        games.screen.add(new_explosion)
        self.destroy()

class Asteroid(Wrapper):
    """ An asteroid which floats across the screen. """
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    POINTS = 30
    total = 0
    Asteroid.total += 1
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
        self.game = game

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
        # check if missile overlaps any other object
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()

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

class Ship(Wrapper):
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
    # cap velocity in each direction
    self.dx = min(max(self.dx, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
    self.dy = min(max(self.dy, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
    # create the ship
    the_ship = Ship(image = Ship(image = Ship.image,
    x = games.screen.width/2
    y = games.screen.height/2)
    games.screen.add(the_ship))
    def __init__(self, x, y):
        """ Initialize ship sprite. """
        super(Ship, self).__init__(image = Ship.image, x = x, y = y)
        self.missile_wait = 0
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
        # if waiting until the ship can fire next, decrease wait
        if self.missile_wait > 0:
            self.missile_wait -= 1
        # fire missile if spacebar pressed and missile wait is over
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait = 0:
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)
            self.missile_wait = Ship.MISSILE_DELAY
    def die(self):
        """ Destroy ship and end game. """
        self.game.end()
        super(Ship, self).die()


# The Missile Class
class Missile(Collider):
    """ A missile launched by the player's ship. """
    image = games.load_image("missile.bmp")
    sound = games.load_sound("missile.wav")
    BUFFER = 40
    VELOCITY_FACTOR = 7
    LIFETIME = 40
    MISSILE_DELAY = 25
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
        def die(self):
            """ Destroy the missile. """
            self.destroy()
        # check if ship overlaps any other object
        if self.overlapping_sprites:
            if self.overlapping_sprites:
                for sprite in self.overlapping_sprites:
                    sprite.die()
                super(Asteroid, self).die()
                super(Missile, self).update()

class Explosion(games.Animation):
    """ Explosion Animation."""
    sound = games.load_sound("explosion.wav")
    explosion_files = ["explosion1.bmp",
    "explosion2.bmp",
    "explosion3.bmp",
    "explosion4.bmp",
    "explosion5.bmp",
    "explosion6.bmp",
    "explosion7.bmp",
    "explosion8.bmp",
    "explosion9.bmp"]
    def __init__(self, x, y):
        super(Explosion, self).__init__(images = Explosion.images,
        x = x, y = y, repeat_interval = 4, n_repeats = 1, is_collideable = False)

# kick it off!
main()