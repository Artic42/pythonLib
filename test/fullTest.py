import dateTimeTest
import articLoggerTest
import sqliteEngineTest
import diceTest
import fileIOTest
from articlib.testEngine import test


def main():
    dateTimeTest.runTest()
    articLoggerTest.runTest()
    sqliteEngineTest.runTest()
    diceTest.runTest()
    fileIOTest.runTest()
    test.printResults()


if __name__ == "__main__":
    main()
