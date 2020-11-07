# Standard library imports
from pathlib import Path
from sys import path

base_path: str = 'C:/projects'
project_path: str = str(Path(base_path).resolve())
path.insert(0, project_path)

print(path)

# import organization libraries

blue_laser: Path = Path('../images/laserBlue01.png')
player_ship: Path = Path('../images/playerShip1_orange.png')
small_asteroid: Path = Path('../images/meteorGrey_small1.png')
medium_asteroid: Path = Path('../images/meteorGrey_med1.png')
large_asteroid: Path = Path('../images/meteorGrey_big1.png')