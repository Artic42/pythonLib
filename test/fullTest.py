import dateTimeTest
import articLoggerTest
import sqliteEngineTest
from articlib.testEngine import test


def main():
    dateTimeTest.runTest()
    articLoggerTest.runTest()
    sqliteEngineTest.runTest()
    test.printResults()
    

if __name__ == "__main__":
    main()