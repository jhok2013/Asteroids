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

    def __init__(self) -> None:
        super().__init__()
        self.radius = BULLET_RADIUS
        self.speed = BULLET_SPEED
        self.life = BULLET_LIFE
        self.image = blue_laser
        self.velocity.dx = cos(radians(self.direction)) * self.speed
        self.velocity.dy = sin(radians(self.direction)) * self.speed
    
    def fire(self, angle: float) -> None:
        pass