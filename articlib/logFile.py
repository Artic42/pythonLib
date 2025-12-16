import logging
import articFileUtils as FU

log = logging.getLogger()


def logFile(path):
    log.info("===============================")
    log.info("   Log contents of file")
    log.info(f"   Path: {path}")
    log.info("===============================")
    if FU.fileExists(path):
        FP = open(path, 'w')
        lines = FP.readlines()
        for line in lines:
            log.info(line)
    else:
        log.error("File doesn't exist")
    log.info("===============================")
