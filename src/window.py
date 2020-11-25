# Standard library imports
from typing import List

# Third party imports
from context import arcade
from context import INITIAL_ROCK_COUNT
from Asteroids import SmallAsteroid, MediumAsteroid, LargeAsteroid
from base import FlyingObject
from Bullets import Bullet
from Ship import Ship

# Organization imports

class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction

    This class will then call the appropriate functions of
    each of the above classes.

    You are welcome to modify anything in this class.
    """

    asteroids: List[FlyingObject] = []
    ship: Ship = Ship()
    bullets: List[Bullet] = []

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)
        self.held_keys = set()
        for i in range(INITIAL_ROCK_COUNT):
            big_asteroid: LargeAsteroid = LargeAsteroid()
            self.asteroids.append(big_asteroid)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        for asteroid in self.asteroids:
            asteroid.draw()
        
        for bullet in self.bullets:
            bullet.draw()
        
        self.ship.draw()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """

        self.check_keys()

        for asteroid in self.asteroids:
            asteroid.advance()
            if asteroid.lives <= 0:
                asteroid.alive = False
            if not asteroid.alive:
                asteroid.break_apart(asteroids=self.asteroids)
                self.asteroids.remove(asteroid)

        for bullet in self.bullets:
            bullet.advance()
            if not bullet.alive:
                self.bullets.remove(bullet)
        
        self.ship.advance()
        self.check_collisions()
    
    def check_collisions(self) -> None:
        '''
        Check for collisions between all different objects
        that have inherited from the FlyingObject class.
        '''
        for bullet in self.bullets:
            for asteroid in self.asteroids:
                if bullet.alive and asteroid.alive:
                    if abs(asteroid.center.x - bullet.center.x) < asteroid.radius + bullet.radius \
                    and abs(asteroid.center.y - bullet.center.y) < asteroid.radius + bullet.radius:
                        # Collision detected
                        bullet.alive = False
                        asteroid.lives -= 1

        for asteroid in self.asteroids:
            if self.ship.alive and asteroid.alive:
                if abs(asteroid.center.x - self.ship.center.x) < asteroid.radius + self.ship.radius \
                and abs(asteroid.center.y - self.ship.center.y) < asteroid.radius + self.ship.radius:
                    # Collision detected
                    self.ship.lives -= 1


    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.left()

        if arcade.key.RIGHT in self.held_keys:
            self.ship.right()

        if arcade.key.UP in self.held_keys:
            self.ship.thrust(is_up=True)

        if arcade.key.DOWN in self.held_keys:
            self.ship.thrust(is_up=False)

        # Machine gun mode...
        #if arcade.key.SPACE in self.held_keys:
        #    pass


    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                bullet: Bullet = Bullet(
                    ship_angle=self.ship.angle,
                    ship_x=self.ship.center.x,
                    ship_y=self.ship.center.y
                )
                self.bullets.append(bullet)
                bullet.fire(self.ship.angle)

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)