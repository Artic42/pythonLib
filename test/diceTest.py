from articlib.testEngine import test
import articlib.dice as Dice


def runTest():
    print("Dice test starte")
    runScenario1()
    print("Dice test finished")


def runScenario1():
    print("Scenario 1 started")
    dice1 = Dice.dice(1)
    test.testIfEqual(dice1.roll(), 1, "Roll 1 dice")
    customDice = Dice.customDice(["A", "A", "A", "A"])
    test.testIfEqual(customDice.roll(), "A", "Roll 1 custom dice")
    dicePool = Dice.dicePool([dice1, dice1, dice1])
    test.testIfEqual(dicePool.roll(), [1, 1, 1], "Roll 3 dice")
    test.testIfEqual(dicePool.rollSum(), 3, "Add the 3")
    test.testIfEqual(dicePool.rollSuccesses(2), 0, "Check no succes")
    test.testIfEqual(dicePool.rollSuccesses(1), 3, "Check successes")
    print("Scenario 1 finished")


if __name__ == "__main__":
    runTest()
    test.printResults()