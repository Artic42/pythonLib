import dateTimeTest
import articLoggerTest
from testEngine import test


def main():
    dateTimeTest.runTest()
    articLoggerTest.runTest()
    test.printResults()
    

if __name__ == "__main__":
    main()