import logging
from articlib import articFileUtils as FU


log = logging.getLogger()


def logFile(path: str) -> None:
    log.info("===================================================")
    log.info("   Log contents of file")
    log.info(f"   Path: {path}")
    log.info("===================================================")
    if FU.fileExists(path):
        FP = open(path, "r")
        lines = FP.readlines()
        for line in lines:
            log.info(line[:-1])
    else:
        log.error("File doesn't exist")
    log.info("===================================================")


def logTestStart(title: str) -> None:
    logSepDoubleLine()
    log.info(f"  {title}")
    logSepDoubleLine()


def logTestEnd() -> None:
    logSepDoubleLine()
    log.info("  Test finished")
    logSepDoubleLine()
    log.info("")
    log.info("")


def logSepDoubleLine() -> None:
    log.info("===================================================")


def logSepLine() -> None:
    log.info("---------------------------------------------------")
