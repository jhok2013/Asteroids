# Standard library imports
import arcade

# Organization imports
from window import Game
from settings.constants import SCREEN_WIDTH, SCREEN_HEIGHT

window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()