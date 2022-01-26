from src.items.sulfuras import Sulfuras

sulfuras1 = [
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80],
    ['Sulfuras, Hand of Ragnaros', 0, 80]
]

sulfuras2 = [
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80],
    ['Sulfuras, Hand of Ragnaros', -1, 80]
]

test1 = Sulfuras('Sulfuras, Hand of Ragnaros', 0, 80)
for day in sulfuras1:
    print(test1)
    assert test1.getSelling() == day[1]
    assert test1.getQuality() == day[2]
    test1.updateQuality()

test2 = Sulfuras('Sulfuras, Hand of Ragnaros', -1, 80)
for day in sulfuras2:
    print(test2)
    assert test2.getSelling() == day[1]
    assert test2.getQuality() == day[2]
    test2.updateQuality()