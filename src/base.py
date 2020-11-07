# Standard library imports
from typing import Union, Any
from abc import ABC, abstractmethod

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
    radius: float
    color: Any

    def __init__(self) -> None:
        '''

        '''
        self.alive = True
        self.center = Point()
        self.velocity = Velocity()
        self.radius = 0
        self.color = None

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