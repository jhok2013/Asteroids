# Standard library imports
from typing import Union, Any

# Third party imports


# Organization imports

class Bullet(FlyingObject):
    '''

    '''
    angle: Union[float, int]
    bounce_counter: int

    def __init__(self) -> None:
        super().__init__()
        self.radius = BULLET_RADIUS
        self.color = BULLET_COLOR
        self.angle = 45
        self.bounce_counter = 3
    
    def fire(self, angle: float) -> None:
        self.velocity.dx = cos(radians(angle)) * BULLET_SPEED
        self.velocity.dy = sin(radians(angle)) * BULLET_SPEED
        self.center.y = RIFLE_WIDTH/2 * cos(radians(angle))
        self.center.x = RIFLE_WIDTH/2 * sin(radians(angle))

    def draw(self) -> None:
        '''

        '''
        arcade.draw_circle_filled(
            center_x=self.center.x,
            center_y=self.center.y,
            radius=self.radius,
            color=self.color
        )

    def bounce_horizontal(self) -> None:
        '''

        '''
        self.velocity.dx *= -1
        self.bounce_counter -= 1
        if self.bounce_counter == 0:
            self.alive = False
    
    def bounce_vertical(self) -> None:
        '''

        '''
        self.velocity.dy *= -1
        self.bounce_counter -= 1
        if self.bounce_counter == 0:
            self.alive = False