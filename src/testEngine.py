import articLogger as logger
from consoleUtils import printRed, printGreen, printYellow, printMagenta

class testEngine:
    def __init__(self):
        self.passed = True
        self.failed = False
        self.escenarioPassed = True
        self.escenarioFailed = False
        self.testCount = 0
        self.scenarioCount = 0
        self.passCount = 0
        self.failCount = 0
        self.skipCount = 0
        
    def testIfTrue(self, test, message):
        if self.escenarioPassed:
            self.testCount += 1
            if test:
                self.passCount += 1
                printGreen(f"\tTest {self.testCount} passed: {message}")
                return 1
            else:
                self.failCount += 1
                printRed(f"\tTest {self.testCount} failed: {message}")
                self.scenarioPassed = False
                self.scenarioFailed= True
                return 2
        else:
            self.skipCount += 1
            printYellow(f"\tTest {self.testCount} skipped: {message}")
            return 3
    
    def testIfFalse(self, test, message):
        self.testIfTrue(not test, message)
    
    def testIfEqual(self, expected, testValue, message):
        response = self.testIfTrue(expected == testValue, message)
        if response == 2:
            printMagenta(f"\t\tExpected value equal to {expected}")
            printMagenta(f"\t\tValue equal to {testValue}")
    
    def testIfNotEqual(self, expected, testValue, message):
        response = self.testIftrue(expected != testValue, message)
        if response == 2:
            printMagenta(f"\t\tExpected value differen to {expected}")
            printMagenta(f"\t\tValue equal to {testValue}")
    
    def testIfGreater(self, expected, testValue, message):
        response = self.testIftrue(expected > testValue, message)
        if response == 2:
            printMagenta(f"\t\tExpected value greater than {expected}")
            printMagenta(f"\t\tValue equal to {testValue}")
    
    def testIfGreaterEqual(self, expected, testValue, message):
        response = self.testIftrue(expected >= testValue, message)
        if response == 2:
            printMagenta(f"\t\tExpected value greater or equal than {expected}")
            printMagenta(f"\t\tValue equal to {testValue}")
    
    def testIfLess(self, expected, testValue, message):
        response = self.testIftrue(expected < testValue, message)
        if response == 2:
            printMagenta(f"\t\tExpected value less than {expected}")
            printMagenta(f"\t\tValue equal to {testValue}")
    
    def testIfLessEqual(self, expected, testValue, message):
        response = self.testIftrue(expected <= testValue, message)
        if response == 2:
            printMagenta(f"\t\tExpected value less or equal than {expected}")
            printMagenta(f"\t\tValue equal to {testValue}")
        
    def newScenario(self, name):
        self.scenarioCount += 1
        print(f"Starting scenario {self.scenarioCount}: {name}")
        
    def endScenario(self, name):
        if self.escenarioPassed:
            print(f"Scenario {self.scenarioCount}:{name} ended with result: PASSED")
        else:
            print(f"Scenario {self.scenarioCount}:{name} ended with result: FAILED")
        if self.escenarioFailed:
            self.passed = False
            self.failed = True
        self.escenarioPassed = True
        self.escenarioFailed = False
        
        
    # Output test results in different ways
    def printResults(self):
        if self.passed:
            printGreen("TEST PASSED")
        else:
            printRed("TEST FAILED")
        print(f"\t {self.scenarioCount} scenarios")
        print(f"\t {self.testCount} tests")
        print(f"\t {self.passCount} passed")
        print(f"\t {self.failCount} failed")
        print(f"\t {self.skipCount} skipped")
        
    def lofResults(self, log):
        if self.passed:
            logger.addEntry("TEST PASSED", log.INFO_MASK)
        else:
            logger.addEntry("TEST FAILED", log.ERROR_MASK)
        logger.addEntry(f"\t {self.passCount} passed\n")
        logger.addEntry(f"\t {self.failCount} failed\n")
        logger.addEntry(f"\t {self.skipCount} skipped\n")
        logger.addEntry(f"\t {self.testCount} total\n")
    

test = testEngine()