from src.items.normalItem import normalItem

dexVest = [
    ['+5 Dexterity Vest', 10, 20],
    ['+5 Dexterity Vest', 9, 19],
    ['+5 Dexterity Vest', 8, 18],
    ['+5 Dexterity Vest', 7, 17],
    ['+5 Dexterity Vest', 6, 16],
    ['+5 Dexterity Vest', 5, 15],
    ['+5 Dexterity Vest', 4, 14],
    ['+5 Dexterity Vest', 3, 13],
    ['+5 Dexterity Vest', 2, 12],
    ['+5 Dexterity Vest', 1, 11],
    ['+5 Dexterity Vest', 0, 10],
    ['+5 Dexterity Vest', -1, 8],
    ['+5 Dexterity Vest', -2, 6],
    ['+5 Dexterity Vest', -3, 4],
    ['+5 Dexterity Vest', -4, 2],
    ['+5 Dexterity Vest', -5, 0],
    ['+5 Dexterity Vest', -6, 0],
    ['+5 Dexterity Vest', -7, 0],
    ['+5 Dexterity Vest', -8, 0],
    ['+5 Dexterity Vest', -9, 0],
    ['+5 Dexterity Vest', -10, 0],
    ['+5 Dexterity Vest', -11, 0],
    ['+5 Dexterity Vest', -12, 0],
    ['+5 Dexterity Vest', -13, 0],
    ['+5 Dexterity Vest', -14, 0],
    ['+5 Dexterity Vest', -15, 0],
    ['+5 Dexterity Vest', -16, 0],
    ['+5 Dexterity Vest', -17, 0],
    ['+5 Dexterity Vest', -18, 0],
    ['+5 Dexterity Vest', -19, 0]
]
test1 = normalItem('+5 Dexterity Vest', 10, 20)
for day in dexVest:
    print(test1)
    assert test1.getSelling() == day[1]
    assert test1.getQuality() == day[2]
    test1.updateQuality()


    