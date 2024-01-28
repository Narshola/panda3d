class MapManager():
    def __init__(self, base):
        self.base = base
        self.model = './m5u1/block.egg'
        self.texture = './m5u1/block.png'
        self.color = (0.2,0.2,0.35,1)
        self.startNew()
        self.addBlock((0,0,0))
        self.addBlock((0,10,0))

    def startNew(self):
        self.land = self.base.render.attachNewNode("Land")

    def addBlock(self, position):
        self.block = self.base.loader.loadModel(self.model)
        self.block.setTexture(self.base.loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)