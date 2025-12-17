import logging
from articlib import logUtils

log = logging.getLogger()

TEST_FILE = "test/files/testFile"


def test_logFile():
    logUtils.logTestStart("Log file test")
    logUtils.logFile(TEST_FILE)
    logUtils.logFile(TEST_FILE, debugFlag = True)
    logUtils.logTestEnd()
