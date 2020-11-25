# Standard library imports
from typing import Union, Any
from math import radians, cos, sin, atan2
from pathlib import Path

# Third party imports


# Organization imports
from context import arcade, BULLET_RADIUS, BULLET_SPEED, BULLET_LIFE, blue_laser #type: ignore
from base import FlyingObject

class Bullet(FlyingObject):
    '''

    '''

    def __init__(
        self, 
        ship_angle, 
        ship_x: Union[float, int], 
        ship_y: Union[float, int]) -> None:
        '''

        '''
        # Initialize parent class
        super().__init__()

        # Initialize starting attributes
        self.radius = BULLET_RADIUS
        self.speed = BULLET_SPEED
        self.life = BULLET_LIFE
        self.center.x = ship_x
        self.center.y = ship_y

        # Image attributes
        self.image = blue_laser
        self.angle = ship_angle - 90
        self.texture = arcade.load_texture(self.image)
        self.width = self.texture.width
        self.height = self.texture.height
    
    def fire(self, angle: float) -> None:
        '''

        '''

        self.velocity.dx -= sin(
            radians(
                self.angle + 90
            )
        ) * self.speed

        self.velocity.dy += cos(
            radians(
                self.angle + 90
            )
        ) * self.speed
    
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
            alpha=100
        )

    def advance(self) -> None:
        '''

        '''
        super().advance()
        self.life -= 1
        if self.life <= 0:
            self.alive = False