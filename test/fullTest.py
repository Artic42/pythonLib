import dateTimeTest
import sqliteEngineTest
import diceTest
import fileIOTest
from articlib.testEngine import testEngine
from articlib.articLogger import Logger


def main():
    test = testEngine.getInstance()
    dateTimeTest.runTest()
    # articLoggerTest.runTest()
    sqliteEngineTest.runTest()
    diceTest.runTest()
    fileIOTest.runTest()
    test.printResults()


if __name__ == "__main__":
    test = testEngine(outputConsole=True, outputLog=True)
    log = Logger()
    log.initialize("fullTest", 1000, "logs", Logger.DEFAULT_MASK, consoleOutput=True)
    log.addEntry("Starting full test suite", Logger.INFO_MASK)
    main()
