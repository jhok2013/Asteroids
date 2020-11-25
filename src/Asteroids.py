# Standard library imports
from typing import Union, Any, List
from random import randint
from math import radians, cos, sin, atan2

# Third party imports

# Organization imports
from base import FlyingObject
from context import small_asteroid, medium_asteroid, large_asteroid #type: ignore
from context import BIG_ROCK_RADIUS, BIG_ROCK_SPEED, BIG_ROCK_SPIN #type: ignore
from context import MEDIUM_ROCK_RADIUS, MEDIUM_ROCK_SPIN #type: ignore
from context import ALPHA
from context import SMALL_ROCK_RADIUS, SMALL_ROCK_SPIN #type: ignore
from context import arcade #type: ignore

class SmallAsteroid(FlyingObject):
    '''

    '''

    def __init__(self) -> None:
        '''

        '''
        super().__init__()
        self.image = small_asteroid
        self.texture = arcade.load_texture(self.image)
        self.width = self.texture.width
        self.height = self.texture.height
        self.center.x = randint(1, 50)
        self.center.y = randint(1, 150)
        self.direction = randint(1, 50)
        self.speed = BIG_ROCK_SPEED
        self.spin = SMALL_ROCK_SPIN
        self.radius = SMALL_ROCK_RADIUS
        self.velocity.dx = cos(radians(self.direction)) * self.speed
        self.velocity.dy = sin(radians(self.direction)) * self.speed
        self.lives = 1

    def advance(self) -> None:
        '''

        '''
        super().advance()
        self.angle += self.spin

    def draw(self) -> None:
        '''

        '''
        arcade.draw_texture_rectangle(
            center_x=self.center.x,
            center_y=self.center.y,
            width=self.width,
            height=self.height,
            texture=self.texture,
            angle=self.angle,
            alpha=ALPHA
        )
    
    def break_apart(self, asteroids: List[FlyingObject]) -> None:
        '''

        '''
        pass

class MediumAsteroid(FlyingObject):
    '''

    '''
    def __init__(self) -> None:
        '''

        '''
        super().__init__()
        self.image = medium_asteroid
        self.texture = arcade.load_texture(self.image)
        self.width = self.texture.width
        self.height = self.texture.height
        self.center.x = randint(1, 50)
        self.center.y = randint(1, 150)
        self.direction = randint(1, 50)
        self.speed = BIG_ROCK_SPEED
        self.spin = MEDIUM_ROCK_SPIN
        self.radius = MEDIUM_ROCK_RADIUS
        self.velocity.dx = cos(radians(self.direction)) * self.speed
        self.velocity.dy = sin(radians(self.direction)) * self.speed
        self.lives = 2

    def draw(self) -> None:
        '''

        '''
        arcade.draw_texture_rectangle(
            center_x=self.center.x,
            center_y=self.center.y,
            width=self.width,
            height=self.height,
            texture=self.texture,
            angle=self.angle,
            alpha=ALPHA
        )

    def advance(self) -> None:
        '''

        '''
        super().advance()
        self.angle += self.spin
    
    def break_apart(self, asteroids: List[FlyingObject]) -> None:
        '''

        '''
        small_asteroid: SmallAsteroid = SmallAsteroid()
        small_asteroid.center.x = self.center.x
        small_asteroid.center.y = self.center.y
        small_asteroid.velocity.dy = self.velocity.dy + 5
        for i in range(1, 2):
            asteroids.append(small_asteroid)

class LargeAsteroid(FlyingObject):
    '''

    '''

    def __init__(self) -> None:
        '''

        '''
        super().__init__()
        self.lives = 3
        self.image = large_asteroid
        self.texture = arcade.load_texture(self.image)
        self.width = self.texture.width
        self.height = self.texture.height
        self.center.x = randint(1, 50)
        self.center.y = randint(1, 150)
        self.direction = randint(1, 50)
        self.speed = BIG_ROCK_SPEED
        self.spin = BIG_ROCK_SPIN
        self.radius = BIG_ROCK_RADIUS
        self.velocity.dx = cos(radians(self.direction)) * self.speed
        self.velocity.dy = sin(radians(self.direction)) * self.speed

    def draw(self) -> None:
        '''

        '''
        arcade.draw_texture_rectangle(
            center_x=self.center.x,
            center_y=self.center.y,
            width=self.width,
            height=self.height,
            texture=self.texture,
            angle=self.angle,
            alpha=ALPHA
        )    

    def advance(self) -> None:
        '''

        '''
        super().advance()
        self.angle += self.spin

    def break_apart(self, asteroids: List[FlyingObject]) -> None:
        '''

        '''
        medium_asteroid: MediumAsteroid = MediumAsteroid()
        medium_asteroid.center.x = self.center.x
        medium_asteroid.center.y = self.center.y
        medium_asteroid.velocity.dy = self.velocity.dy + 5
        for i in range(1, 2):
            asteroids.append(medium_asteroid)