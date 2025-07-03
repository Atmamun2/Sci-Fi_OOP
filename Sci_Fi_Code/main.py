import settings, setup
from settings import Location, DamagedMaintenanceDroid
from utils import DiagnosticTool, EnergyCrystal
from setup import GameController

if __name__ == "__main__":
    Game = GameController()
    Game.start_game()