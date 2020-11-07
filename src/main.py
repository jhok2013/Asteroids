# Standard library imports

# Organization imports
from window import Game #type: ignore
from context import SCREEN_HEIGHT, SCREEN_WIDTH, arcade #type: ignore

window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()