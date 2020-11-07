# Standard library imports
from typing import Union, Any
from math import radians, cos, sin, atan2

# Third party imports


# Organization imports
from context import arcade, BULLET_RADIUS, BULLET_SPEED, BULLET_LIFE #type: ignore
from base import FlyingObject

class Bullet(FlyingObject):
    '''

    '''
    angle: Union[float, int]

    def __init__(self) -> None:
        super().__init__()
        self.radius = BULLET_RADIUS
    
    def fire(self, angle: float) -> None:
        self.velocity.dx = cos(radians(angle)) * BULLET_SPEED
        self.velocity.dy = sin(radians(angle)) * BULLET_SPEED

    def draw(self) -> None:
        '''

        '''
        pass