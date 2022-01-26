from src.items.conjured import Conjured

manaCake = [
    ['Conjured Mana Cake', 3, 20],
    ['Conjured Mana Cake', 2, 18],
    ['Conjured Mana Cake', 1, 16],
    ['Conjured Mana Cake', 0, 14],
    ['Conjured Mana Cake', -1, 10],
    ['Conjured Mana Cake', -2, 6],
    ['Conjured Mana Cake', -3, 2],
    ['Conjured Mana Cake', -4, 0],
    ['Conjured Mana Cake', -5, 0],
    ['Conjured Mana Cake', -6, 0],
    ['Conjured Mana Cake', -7, 0],
    ['Conjured Mana Cake', -8, 0],
    ['Conjured Mana Cake', -9, 0],
    ['Conjured Mana Cake', -10, 0],
    ['Conjured Mana Cake', -11, 0],
    ['Conjured Mana Cake', -12, 0],
    ['Conjured Mana Cake', -13, 0],
    ['Conjured Mana Cake', -14, 0],
    ['Conjured Mana Cake', -15, 0],
    ['Conjured Mana Cake', -16, 0],
    ['Conjured Mana Cake', -17, 0],
    ['Conjured Mana Cake', -18, 0],
    ['Conjured Mana Cake', -19, 0],
    ['Conjured Mana Cake', -20, 0],
    ['Conjured Mana Cake', -21, 0],
    ['Conjured Mana Cake', -22, 0],
    ['Conjured Mana Cake', -23, 0],
    ['Conjured Mana Cake', -24, 0],
    ['Conjured Mana Cake', -25, 0],
    ['Conjured Mana Cake', -26, 0]
]

test1 = Conjured('Conjured Mana Cake', 3, 20)
for day in manaCake:
    print(test1)
    assert test1.getSelling() == day[1]
    assert test1.getQuality() == day[2]
    test1.updateQuality()