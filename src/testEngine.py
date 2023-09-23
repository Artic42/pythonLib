import articLogger as logger

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
                print(f"\tTest {self.testCount} passed: {message}")
                return 1
            else:
                self.failCount += 1
                print(f"\tTest {self.testCount} failed: {message}")
                self.scenarioPassed = False
                self.scenarioFailed= True
                return 2
        else:
            self.skipCount += 1
            print(f"\tTest {self.testCount} skipped: {message}")
            return 3
    
    def testIfFalse(self, test, message):
        self.testIfTrue(not test, message)
    
    def testIfEqual(self, expected, testValue, message):
        response = self.testIfTrue(expected == testValue, message)
        if response == 2:
            print(f"\t\tExpected value equal to {expected}")
            print(f"\t\tValue equal to {testValue}")
    
    def testIfNotEqual(self, expected, testValue, message):
        response = self.testIftrue(expected != testValue, message)
        if response == 2:
            print(f"\t\tExpected value differen to {expected}")
            print(f"\t\tValue equal to {testValue}")
    
    def testIfGreater(self, expected, testValue, message):
        response = self.testIftrue(expected > testValue, message)
        if response == 2:
            print(f"\t\tExpected value greater than {expected}")
            print(f"\t\tValue equal to {testValue}")
    
    def testIfGreaterEqual(self, expected, testValue, message):
        response = self.testIftrue(expected >= testValue, message)
        if response == 2:
            print(f"\t\tExpected value greater or equal than {expected}")
            print(f"\t\tValue equal to {testValue}")
    
    def testIfLess(self, expected, testValue, message):
        response = self.testIftrue(expected < testValue, message)
        if response == 2:
            print(f"\t\tExpected value less than {expected}")
            print(f"\t\tValue equal to {testValue}")
    
    def testIfLessEqual(self, expected, testValue, message):
        response = self.testIftrue(expected <= testValue, message)
        if response == 2:
            print(f"\t\tExpected value less or equal than {expected}")
            print(f"\t\tValue equal to {testValue}")
        
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
            string = "TEST PASSED"
        else:
            string = "TEST FAILED"
        print(f"Test results: {string}")
        print(f"\t {self.scenarioCount} scenarios")
        print(f"\t {self.testCount} tests")
        print(f"\t {self.passCount} passed")
        print(f"\t {self.failCount} failed")
        print(f"\t {self.skipCount} skipped")
        
    def lofResults(self, log):
        if self.passed:
            string = "TEST PASSED"
        else:
            string = "TEST FAILED"
        logger.addEntry(f"Test results: {string}\n", log.ERROR_MASK)
        logger.addEntry(f"\t {self.passCount} passed\n")
        logger.addEntry(f"\t {self.failCount} failed\n")
        logger.addEntry(f"\t {self.skipCount} skipped\n")
        logger.addEntry(f"\t {self.testCount} total\n")
    

test = testEngine()