import articLogger as logger
import articFileUtils as fileUtils
import testEngine as testEngine
from testEngine import test


def runTest():
    print("Starting test for logger")
    runScenario1()

    

def runScenario1():
    test11()


def test11():
    #Create a log send 1 line and check file size is equal to 3 lines.
    #Title line, 1 message, empty line
    #Also sends a line out of mask and ensure doesn't write
    log1 = logger.Log("log", mask=logger.INFO_MASK)
    log1.log ("Just some log message")
    log1.log ("Just a line to not show", mask=logger.DEBUG_MASK)
    log1.flush()
    pathToLog = log1.getLogFilePath()
    log1File = fileUtils.FileIO(pathToLog, readIt=True)
    test.testIfEqual(2, log1File.lineCount(), "Checking logging in MASK and out of MASK")
    log1.close()
    del log1
    fileUtils.deleteFile(pathToLog)
    
def test12():
    pass
    
if __name__ == "__main__":
    runTest()
    test.printResults()

