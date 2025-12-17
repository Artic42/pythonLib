import logging
from articlib import logFile

log = logging.getLogger()

TEST_FILE = "test/files/testFile"


def test_logFile():
    log.info("===================================================")
    log.info("  Log file test")
    log.info("===================================================")
    logFile.logFile(TEST_FILE)
    log.info("===================================================")
    log.info("  Test finished")
    log.info("===================================================")
    log.info("")
    log.info("")
