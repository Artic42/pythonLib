import articLogger as logger


class testEngine:
    def __init__(self):
        self.passed = True
        self.failed = False
        self.escenarioPassed = True
        self.escenarioFailed = False
        self.testCount = 0
        self.passCount = 0
        self.failCount = 0
        self.skipCount = 0
        
    def testIfTrue(self, test, message):
        if self.escenarioPassed:
            self.testCount += 1
            if test:
                self.passCount += 1
                print(f"Test {self.testCount} passed: {message}")
            else:
                self.failCount += 1
                print(f"Test {self.testCount} failed: {message}")
                self.scenarioPassed = False
                self.scenarioFailed= True
        else:
            self.skipCount += 1
            print(f"Test {self.testCount} skipped: {message}")
    
    def testIfFalse(self, test, message):
        self.testIfTrue(not test, message)
    
    def testIfEqual(self, test1, test2, message):
        self.testIfTrue(test1 == test2, message)
    
    def testIfNotEqual(self, test1, test2, message):
        self.testIfTrue(test1 != test2, message)
    
    def testIfGreater(self, test1, test2, message):
        self.testIfTrue(test1 > test2, message)
    
    def testIfGreaterEqual(self, test1, test2, message):
        self.testIfTrue(test1 >= test2, message)
    
    def testIfLess(self, test1, test2, message):
        self.testIfTrue(test1 < test2, message)
    
    def testIfLessEqual(self, test1, test2, message):
        self.testIfTrue(test1 <= test2, message)
        
    def newScenario(self, name):
        print(f"Starting scenario {name}")
        
    def endScenario(self, name):
        if self.escenarioPassed:
            print(f"Scenario {name} passed")
        else:
            print(f"Scenario {name} failed")
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
        print(f"Test results: {string}\n")
        print(f"\t {self.passCount} passed\n")
        print(f"\t {self.failCount} failed\n")
        print(f"\t {self.skipCount} skipped\n")
        print(f"\t {self.testCount} total\n")
        
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
    
    