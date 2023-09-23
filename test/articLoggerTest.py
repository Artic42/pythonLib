import articLogger as logger
import articFileUtils as fileUtils
import testEngine as testEngine
import time
from testEngine import test



def runTest():
    print("Starting test for logger")
    runScenario1()

    

def runScenario1():
    test.newScenario("Log create, close and masks")
    test11()
    test12_15()
    test16()
    test.endScenario("Log create, close and masks")


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
    
def test12_15():
    #Check if masks are changed correctly
    log1 = logger.Log("logs", mask=logger.INFO_MASK)
    test.testIfEqual(logger.INFO_MASK, log1.getMask(), "Checking mask value is INFO_MASK")
    log1.setValueInMask(logger.DEBUG_MASK)
    test.testIfEqual(logger.INFO_MASK | logger.DEBUG_MASK, log1.getMask(), "Checking mask value is INFO_MASK | DEBUG_MASK")
    log1.unsetValueInMask(logger.DEBUG_MASK)
    test.testIfEqual(logger.INFO_MASK, log1.getMask(), "Checking mask value is INFO_MASK")
    log1.setMask(logger.DEBUG_MASK)
    test.testIfEqual(logger.DEBUG_MASK, log1.getMask(), "Checking mask value is DEBUG_MASK")
    logFilePath = log1.getLogFilePath()
    log1.close()
    fileUtils.deleteFile(logFilePath)
    
def test16():
    log1 = logger.Log("logs", mask=logger.INFO_MASK, maxLines=2)
    log1.log ("Just some log message1")
    time.sleep(2)
    log1.log ("Just some log message2")
    log1.log ("Just some log message3")
    test.testIfEqual(2, len(fileUtils.getFilesInDirectory("logs")), "Checking two log files are created")
    for path in fileUtils.getFilesInDirectory("logs"):
        fileUtils.deleteFile("logs/" + path)
    
    
    
if __name__ == "__main__":
    runTest()
    test.printResults()

