from articlib.consoleUtils import (
    printGreen,
    printYellow,
    printMagenta,
    printGreenBold,
    printRedBold,
)
from articlib.articLogger import Logger

log = Logger.getInstance()


class testEngine:
    __instance = None
    """Singleton test engine class for managing tests and scenarios"""

    @staticmethod
    def getInstance():
        """Static access method to get the singleton instance"""
        if testEngine.__instance is None:
            testEngine.__instance = testEngine()
        return testEngine.__instance

    def __init__(self, outputConsole=True, outputLog=True):
        self.passed = True
        self.failed = False
        self.escenarioPassed = True
        self.escenarioFailed = False
        self.testCount = 0
        self.scenarioCount = 0
        self.passCount = 0
        self.failCount = 0
        self.skipCount = 0
        self.outputConsole = outputConsole
        self.outputLog = outputLog

    def testIfTrue(self, test, message):
        if self.escenarioPassed:
            self.testCount += 1
            if test:
                self.passCount += 1
                self.outputGreen(f"\tTest {self.testCount} passed: {message}")
                return 1
            else:
                self.failCount += 1
                self.outputMagenta(f"\tTest {self.testCount} failed: {message}")
                self.scenarioPassed = False
                self.scenarioFailed = True
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
            self.outputMagenta(f"\t\tExpected value equal to {expected}")
            self.outputMagenta(f"\t\tValue equal to {testValue}")

    def testIfNotEqual(self, expected, testValue, message):
        response = self.testIfTrue(expected != testValue, message)
        if response == 2:
            self.outputMagenta(f"\t\tExpected value different to {expected}")
            self.outputMagenta(f"\t\tValue equal to {testValue}")

    def testIfGreater(self, expected, testValue, message):
        response = self.testIfTrue(expected > testValue, message)
        if response == 2:
            self.outputMagenta(f"\t\tExpected value greater than {expected}")
            self.outputMagenta(f"\t\tValue equal to {testValue}")

    def testIfGreaterEqual(self, expected, testValue, message):
        response = self.testIfTrue(expected >= testValue, message)
        if response == 2:
            self.outputMagenta(
                f"""\t\tExpected value greater
                         or equal than {expected}"""
            )
            self.outputMagenta(f"\t\tValue equal to {testValue}")

    def testIfLess(self, expected, testValue, message):
        response = self.testIfTrue(expected < testValue, message)
        if response == 2:
            self.outputMagenta(f"\t\tExpected value less than {expected}")
            self.outputMagenta(f"\t\tValue equal to {testValue}")

    def testIfLessEqual(self, expected, testValue, message):
        response = self.testIfTrue(expected <= testValue, message)
        if response == 2:
            self.outputMagenta(f"\t\tExpected value less or equal than {expected}")
            self.outputMagenta(f"\t\tValue equal to {testValue}")

    def newScenario(self, name):
        self.scenarioCount += 1
        self.outputDefault(f"Starting scenario {self.scenarioCount}: {name}")

    def endScenario(self, name):
        if self.escenarioPassed:
            self.outputDefault(
                f"""Scenario {self.scenarioCount}:{name} ended
                  with result: PASSED"""
            )
        else:
            self.outputDefault(
                f"""Scenario {self.scenarioCount}:{name} ended
                  with result: FAILED"""
            )
        if self.escenarioFailed:
            self.passed = False
            self.failed = True
        self.escenarioPassed = True
        self.escenarioFailed = False

    # Output test results in different ways
    def outputMagenta(self, message):
        if self.outputConsole:
            printMagenta(message)
        if self.outputLog:
            log.addEntry(message, Logger.ERROR_MASK, consoleOutput=False)

    def outputGreen(self, message):
        if self.outputConsole:
            printGreen(message)
        if self.outputLog:
            log.addEntry(message, Logger.INFO_MASK, consoleOutput=False)

    def outputYellow(self, message):
        if self.outputConsole:
            printYellow(message)
        if self.outputLog:
            log.addEntry(message, Logger.WARN_MASK, consoleOutput=False)

    def outputDefault(self, message):
        if self.outputConsole:
            print(message)
        if self.outputLog:
            log.addEntry(message, Logger.INFO_MASK, consoleOutput=False)

    def printResults(self):
        if self.passed:
            printGreenBold("TEST PASSED")
        else:
            printRedBold("TEST FAILED")
        print(f"\t {self.scenarioCount} scenarios")
        print(f"\t {self.testCount} tests")
        print(f"\t {self.passCount} passed")
        print(f"\t {self.failCount} failed")
        print(f"\t {self.skipCount} skipped")

    def logResults(self):
        if self.passed:
            log.addEntry("TEST PASSED", Logger.INFO_MASK, consoleOutput=False)
        else:
            log.addEntry("TEST FAILED", Logger.ERROR_MASK, consoleOutput=False)
        log.addEntry(f"\t {self.passCount} passed\n", Logger.INFO_MASK, consoleOutput=False)
        log.addEntry(f"\t {self.failCount} failed\n", Logger.INFO_MASK, consoleOutput=False)
        log.addEntry(f"\t {self.skipCount} skipped\n", Logger.INFO_MASK, consoleOutput=False)
        log.addEntry(f"\t {self.testCount} total\n", Logger.INFO_MASK, consoleOutput=False)
