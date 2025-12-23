import articlib.dice as Dice


def test_dice_size1():
    dice1 = Dice.dice(1)
    assert dice1.roll() == 1


def test_custom_dice():
    customDice = Dice.customDice(["A", "A", "A"], "A dice")
    assert customDice.roll() == "A"


def test_dicePools():
    dice1 = Dice.dice(1)
    dicePool = Dice.dicePool([dice1, dice1, dice1])
    assert dicePool.roll() == [1, 1, 1]
    assert dicePool.rollSum() == 3
    assert dicePool.rollSuccesses(2) == 0
    assert dicePool.rollSuccesses(1) == 3


def test_checkLimits():
    size1 = 6
    size2 = 20
    repeats = 1000
    dice = Dice.dice(size1, log=False)
    rollAndCheck(dice, size1, repeats)
    dice.setSize(size2)
    rollAndCheck(dice, size2, repeats)


def rollAndCheck(dice, size, repeats):
    for _ in range(repeats):
        result = dice.roll()
        assert result <= size
        assert result > 0
