import itertools

import articlib.dice as Dice
from articlib import logUtils as LU


def test_dice_size1():
    LU.logTestStart("Size 1 dice test - roll a die with only on side")
    dice1 = Dice.dice(1)
    assert dice1.roll() == 1
    LU.logTestEnd()


def test_custom_dice():
    LU.logTestStart("Custom die test, all sides same value")
    customDice = Dice.customDice(["A", "A", "A"], "A dice")
    assert customDice.roll() == "A"
    LU.logTestEnd()


def test_dicePools():
    LU.logTestStart("Dice pool check, using all one sided dices")
    dice1 = Dice.dice(1)
    dicePool = Dice.dicePool([dice1, dice1, dice1])
    assert dicePool.roll() == [1, 1, 1]
    assert dicePool.rollSum() == 3
    assert dicePool.rollSuccesses(2) == 0
    assert dicePool.rollSuccesses(1) == 3
    LU.logTestEnd()


def test_checkLimits():
    LU.logTestStart("Numeric dice test - 100 rolls in D6 and D20")
    size1 = 6
    size2 = 20
    repeats = 1000
    dice = Dice.dice(size1, log=False)
    rollAndCheck(dice, size1, repeats)
    dice.setSize(size2)
    rollAndCheck(dice, size2, repeats)
    LU.logTestEnd()


def rollAndCheck(dice, size, repeats):
    for _ in range(repeats):
        result = dice.roll()
        assert result <= size
        assert result > 0
