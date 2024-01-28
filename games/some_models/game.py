from direct.showbase.ShowBase import ShowBase

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.model = self.loader.loadModel("Boeing707.egg")
        self.texture = self.loader.loadTexture("BoeingTexture.tif")
        self.model.setTexture(self.texture)
        self.model.setColor((0.3,0.0,0.5,1))
        self.model.reparentTo(self.render)
        self.model.setScale(0.2)
        self.model.setPos(-2,10,-3)
        self.camLens.setFov(90)

game = Game()
game.run()