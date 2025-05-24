import articlib.articFileUtils as AFU
from articlib.testEngine import testEngine
from articlib.articLogger import Logger

test = testEngine.getInstance()


def runTest():
    print("Dice test started")
    runScenario1()
    print("Dice test finished")


def runScenario1():
    print("Scenario 1 started")
    file = AFU.FileIO("test.txt")
    file.addLine("Hello")
    file.removeLastLine()
    test.testIfEqual(file.lines, [], "Remove last line")
    file.addLine("Hello")
    file.addLine("World")
    file.removeLine(0)
    test.testIfEqual(file.lines, ["World"], "Remove first line")
    file.writeFile()
    file = AFU.FileIO("test.txt", True)
    test.testIfEqual(file.lines, ["World"], "Read file")
    file.findAndReplace("World", "Hello")
    test.testIfEqual(file.lines, ["Hello"], "Find and replace")
    AFU.deleteFile("test.txt")
    print("Scenario 1 finished")


if __name__ == "__main__":
    log = Logger(initialize=False)
    log.initialize("fileIOTest", 1000, "logs", Logger.DEFAULT_MASK)
    log.addEntry("Starting file IO test", Logger.INFO_MASK)
    runTest()
    test.printResults()
