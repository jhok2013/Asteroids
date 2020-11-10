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
        self.angle = 1
        self.image = player_ship
        self.center.x = SCREEN_WIDTH/2
        self.center.y = SCREEN_HEIGHT/2
        self.texture = arcade.load_texture(self.image)
        self.width = self.texture.width
        self.height = self.texture.height
    
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
        pass

    def right(self) -> None:
        '''

        '''
        pass

    def thrust(self) -> None:
        '''

        '''
        pass
