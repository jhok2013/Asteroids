# Standard library imports
from typing import Union, Any
from math import radians, cos, sin, atan2

# Third party imports


# Organization imports
from context import arcade, player_ship
from context import SHIP_RADIUS, SHIP_THRUST_AMOUNT, SHIP_TURN_AMOUNT
from context import SCREEN_HEIGHT, SCREEN_WIDTH
from context import ALPHA
from base import FlyingObject

class Ship(FlyingObject):
    '''

    '''

    def __init__(self) -> None:
        '''

        '''
        super().__init__()
        self.angle = 0
        self.image = player_ship
        self.center.x = SCREEN_WIDTH/2
        self.center.y = SCREEN_HEIGHT/2
        self.radius = SHIP_RADIUS
        self.texture = arcade.load_texture(self.image)
        self.width = self.texture.width
        self.height = self.texture.height
        self.lives = 3
    
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

    def left(self) -> None:
        '''

        '''
        self.angle += SHIP_TURN_AMOUNT

    def right(self) -> None:
        '''

        '''
        self.angle -= SHIP_TURN_AMOUNT

    def thrust(self, is_up: bool) -> None:
        '''

        '''
        if is_up:
            self.velocity.dx -= sin(radians(self.angle)) * SHIP_THRUST_AMOUNT
            self.velocity.dy += cos(radians(self.angle)) * SHIP_THRUST_AMOUNT
        else:
            self.velocity.dx += sin(radians(self.angle)) * SHIP_THRUST_AMOUNT
            self.velocity.dy -= cos(radians(self.angle)) * SHIP_THRUST_AMOUNT