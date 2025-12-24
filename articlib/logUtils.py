import logging
import articFileUtils as FU


log = logging.getLogger()


def logFile(path: str, debugFlag: bool = False) -> None:
    if debugFlag is True:
        logFunc = log.debug
    else:
        logFunc = log.info

    logFunc("===================================================")
    logFunc("   Log contents of file")
    logFunc(f"   Path: {path}")
    logFunc("===================================================")
    if FU.fileExists(path):
        FP = open(path, "r")
        lines = FP.readlines()
        for line in lines:
            logFunc(line[:-1])
    else:
        log.error("File doesn't exist")
    logFunc("===================================================")


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
