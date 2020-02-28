# Pizza Panic Game
# Player must catch falling pizzas before they hit the ground.

from livewires import games, colour
import random

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Pna(games.sprite):
    """A pan controleld by player to catch falling pizzas."""
    image = games.load_image("pan.bmp")
    def __init__(self, y = 450):
        """ Initialize Pan object and create Text object for score. """
        super(Pan, self).__init__(image = Pan.image, x = games.mouse.x, y = y)

        self.score = games.Text(value = 0, size = 25, color = color.black, x = 575, y = 20)

        games.screen.add(self.score)
    def update(self):
        """ Move to mouse x position. """
        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0

        if self.right > games.screen.width:
            self.right = games.screen.width

        self.check_catch()
    def check_catch(self):
        """ Check if catch pizzas. """
        for pizza in self.overlapping_sprites:
            self.score.value += 10
            pizza.handle_caught()
class Pizza(games.Sprite):
    """ A pizza which falls to the ground. """
    image = games.load_image("pizza.bmp")
    speed = 1
    def __init__(self, x, y = 90):
        """ Initialize a Pizza object. """
        super(Pizza, self).__init__(image = Pizza.image,
                                    x = x, y = y,
                                    dy = Pizza.speed)
    def update(self):
        """ Check if bottom edge has reached screen bottom. """
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()
    def handle_caught(self):
        """ Destroy self if caught. """
        self.destroy()
    def end_game(self):
        """ End the game. """
        end_message = games.Message(value = "Game Over",
        size = 90, color = color.red, x = games.screen.width/2, y = games.screen.height/2,
        lifetime = 5 * games.screen.fps,
        after_death = games.screen.quit)
        games.screen.add(end_message)
    def check_drop(self):
        """ Decrease countdown or drop pizza and reset countdown. """
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_pizza = Pizza(x = self.x)
            games.screen.add(new_pizza)
        # set so buffer will be 15 pixels, regardless of pizza speed
        self.time_til_drop = int(65 / Pizza.speed)
    def main():
        """ Play the game. """
        wall_image = games.load_image("wall.jpg", transparent = False)
        games.screen.background = wall_image

        the_chef = Chef()
        games.screen.add(the_pan)

        games.mouse.is_visible = False

        games.screen.event_grab = True
        games.screen.mainloop()

# start it up!
main()
