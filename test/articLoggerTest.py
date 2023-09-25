import articLogger as logger
import articFileUtils as fileUtils
import time
from testEngine import test
from articLogger import log

def runTest():
    print("Starting test for logger")
    runScenario1()
    print("Finished test for logger")

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
    log.initialize("log", mask=logger.INFO_MASK)
    log.addEntry("Just some log message")
    log.addEntry("Just a line to not show", mask=logger.DEBUG_MASK)
    log.flush()
    pathToLog = log.getLogFilePath()
    log1File = fileUtils.FileIO(pathToLog, readIt=True)
    test.testIfEqual(2, log1File.lineCount(), "Checking logging in MASK and out of MASK")
    log.close()
    fileUtils.deleteFile(pathToLog)
    
def test12_15():
    #Check if masks are changed correctly
    log.initialize("logs", mask=logger.INFO_MASK)
    test.testIfEqual(logger.INFO_MASK, log.getMask(), "Checking mask value is INFO_MASK")
    log.setValueInMask(logger.DEBUG_MASK)
    test.testIfEqual(logger.INFO_MASK | logger.DEBUG_MASK, log.getMask(), "Checking mask value is INFO_MASK | DEBUG_MASK")
    log.unsetValueInMask(logger.DEBUG_MASK)
    test.testIfEqual(logger.INFO_MASK, log.getMask(), "Checking mask value is INFO_MASK")
    log.setMask(logger.DEBUG_MASK)
    test.testIfEqual(logger.DEBUG_MASK, log.getMask(), "Checking mask value is DEBUG_MASK")
    logFilePath = log.getLogFilePath()
    log.close()
    fileUtils.deleteFile(logFilePath)
    
def test16():
    #Check if when limit reached, new file is created
    log.initialize("logs", mask=logger.INFO_MASK, maxLines=2)
    log.addEntry ("Just some log message1")
    time.sleep(10)
    log.addEntry ("Just some log message2")
    log.addEntry ("Just some log message3")
    test.testIfEqual(2, len(fileUtils.getFilesInDirectory("logs")), "Checking two log files are created")
    for path in fileUtils.getFilesInDirectory("logs"):
        fileUtils.deleteFile("logs/" + path)
    log.close()
    fileUtils.deleteDirectory("logs")
    
if __name__ == "__main__":
    runTest()
    test.printResults()

