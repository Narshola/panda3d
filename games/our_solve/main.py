from direct.showbase.ShowBase import ShowBase
from mapmanager import MapManager

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.land = MapManager(self)

game = Game()
game.run()