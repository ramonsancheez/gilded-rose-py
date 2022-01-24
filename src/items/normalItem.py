from item import item

class normalItem(item):

    def __init__(self, name, quality, sellIn):
        super().__init__(name, quality, sellIn)
    
    def reduceSellIn(self):
        self.sellIn -= 1
    
    def changeQuality(self):
        qualityModified = -1
        if self.quality < 0:
            qualityModified *= 2
        self.quality += qualityModified

    def updateQuality(self):
        self.reduceSellIn()
        self. changeQuality()
    

