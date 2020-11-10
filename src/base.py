# Standard library imports
from typing import Union, Any
from abc import ABC, abstractmethod
from pathlib import Path
from math import radians, sin, cos, atan2

class Point(object):
    '''
    The point with an x and y.
    '''
    x: Union[float, int]
    y: Union[float, int]

    def __init__(self) -> None:
        self.x = 0
        self.y = 0

class Velocity(object):
    '''
    The velocity of an object.
    '''
    dx: Union[float, int]
    dy: Union[float, int]

    def __init__(self) -> None:
        self.dx = 0.00
        self.xy = 0.00       

class FlyingObject(ABC):
    '''

    '''
    alive: bool
    center: Point
    velocity: Velocity
    radius: Union[float, int]
    color: Any
    angle: Union[float, int]
    image: Path
    speed: Union[float, int]
    direction: Union[float, int]

    def __init__(self) -> None:
        '''

        '''
        self.alive = True
        self.center = Point()
        self.velocity = Velocity()
        self.radius = 0
        self.height = 0
        self.width = 0
        self.color = None
        self.angle = 360
        self.speed = 0
        self.direction = 0

    @abstractmethod
    def draw(self) -> None:
        '''

        '''
        pass

    def is_off_screen(self, screen_width: int, screen_height: int) -> bool:
        '''

        '''
        if self.center.x > screen_width or self.center.x < 0 or self.center.y > screen_height or self.center.y < 0:
            return True
        else:
            return False

    def advance(self) -> None:
        '''

        '''
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
    
    def is_alive(self) -> bool:
        '''

        '''
        return self.alive