class gildedRose():
    def __init__(self, items):
        self.stock = items
    
    def add(self, newItem):
        self.stock.append(newItem)