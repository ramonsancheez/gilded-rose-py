from item import item
class agedBrie(item):
    
        def __init__(self, name, quality, sellIn):
            super().__init__(self, name, quality, sellIn)
        
        def improveQuality(self):
            qualifyModifier = 1
            if self.sellIn < 0:
                qualifyModifier *= 2
            self.quality += qualifyModifier 