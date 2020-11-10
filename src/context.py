# Standard library imports
from pathlib import Path
from sys import path
from typing import Union, Any

# 3rd party imports
import arcade #type: ignore

base_path: str = 'C:/projects'
project_path: str = str(Path(base_path).resolve())
path.insert(0, project_path)

# import organization libraries
from settings.constants import *

blue_laser: Path = Path('./src/images/laserBlue01.png').resolve()
player_ship: Path = Path('./src/images/playerShip1_orange.png').resolve()
small_asteroid: Path = Path('./src/images/meteorGrey_small1.png').resolve()
medium_asteroid: Path = Path('./src/images/meteorGrey_med1.png').resolve()
large_asteroid: Path = Path('./src/images/meteorGrey_big1.png').resolve()