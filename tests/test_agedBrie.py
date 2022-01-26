from src.items.agedBrie import AgedBrie

agedBrie = [
    ['Aged Brie', 2, 0],
    ['Aged Brie', 1, 1],
    ['Aged Brie', 0, 2],
    ['Aged Brie', -1, 4],
    ['Aged Brie', -2, 6],
    ['Aged Brie', -3, 8],
    ['Aged Brie', -4, 10],
    ['Aged Brie', -5, 12],
    ['Aged Brie', -6, 14],
    ['Aged Brie', -7, 16],
    ['Aged Brie', -8, 18],
    ['Aged Brie', -9, 20],
    ['Aged Brie', -10, 22],
    ['Aged Brie', -11, 24],
    ['Aged Brie', -12, 26],
    ['Aged Brie', -13, 28],
    ['Aged Brie', -14, 30],
    ['Aged Brie', -15, 32],
    ['Aged Brie', -16, 34],
    ['Aged Brie', -17, 36],
    ['Aged Brie', -18, 38],
    ['Aged Brie', -19, 40],
    ['Aged Brie', -20, 42],
    ['Aged Brie', -21, 44],
    ['Aged Brie', -22, 46],
    ['Aged Brie', -23, 48],
    ['Aged Brie', -24, 50],
    ['Aged Brie', -25, 50],
    ['Aged Brie', -26, 50],
    ['Aged Brie', -27, 50]
]
test1 = AgedBrie('Aged Brie', 2, 0)
for day in agedBrie:
    print(test1)
    assert test1.getSelling() == day[1]
    assert test1.getQuality() == day[2]
    test1.updateQuality()