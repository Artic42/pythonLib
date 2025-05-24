import articlib.dice as Dice
from articlib.testEngine import testEngine
from articlib.articLogger import Logger

test = testEngine.getInstance()


def runTest():
    print("Dice test started")
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
    test.testIfEqual(dicePool.rollSuccesses(2), 0, "Check no successes")
    test.testIfEqual(dicePool.rollSuccesses(1), 3, "Check successes")
    print("Scenario 1 finished")


if __name__ == "__main__":
    log = Logger(initialize=False)
    log.initialize("diceTest", 1000, "logs", Logger.DEFAULT_MASK)
    log.addEntry("Starting dice test", Logger.INFO_MASK)
    runTest()
    test.printResults()
