import articlib.dateTime as dateTime
import os

if __name__ == "__main__":
    pass

INFO_MASK = 0b00000001
WARN_MASK = 0b00000010
ERROR_MASK = 0b00000100
COMMS_SEND_MASK = 0b00001000
COMMS_RECV_MASK = 0b00010000
HERMES_MASK = 0b00100000
COMMS_MASK = 0b00011000
DEBUG_MASK = 0b01000000
DEFAULT_MASK = INFO_MASK | COMMS_MASK | ERROR_MASK | HERMES_MASK


class Logger:
    def __init__(self):
        self.init = False
        self.logName = ""
        self.maxLines = 0
        self.lines = 0
        self.logPath = ""
        self.mask = 0b0

    def initialize(self, logName, maxLines=1000, logPath="logs", mask=DEFAULT_MASK):
        self.init = True
        self.logName = logName
        self.maxLines = maxLines
        self.lines = 0
        self.logPath = logPath
        self.mask = mask
        self.date = dateTime.createDate(dateTime.YYYYMMDD)
        self.createLogFile()

    def createLogFile(self):
        self.date.setToNow()
        dateSring = self.date.getDateTimePathFomat()
        os.makedirs(self.logPath, exist_ok=True)
        self.logFilePath = self.logPath + "/" + self.logName + "_" + dateSring + ".log"
        if os.path.isfile(self.logFilePath):
            self.logFile = open(self.logFilePath, "a")
        else:
            self.logFile = open(self.logFilePath, "w")
            self.logFile.write(
                f"Log file created at {self.date.getDateTime()} with name {self.logName}\n"
            )
            self.lines = 0

    def addEntry(self, message, mask=INFO_MASK):
        maskName = self.getMaskName(mask)
        if mask & self.mask:
            if self.init:
                self.writeLog(message, maskName)

    def getMaskName(self, mask):
        switcher = {
            INFO_MASK: "INFO",
            WARN_MASK: "WARN",
            ERROR_MASK: "ERROR",
            COMMS_SEND_MASK: "COMMS_SEND",
            COMMS_RECV_MASK: "COMMS_RECV",
            HERMES_MASK: "HERMES",
            DEBUG_MASK: "DEBUG",
            DEFAULT_MASK: "DEFAULT",
        }
        return switcher.get(mask, "UNKNOWN")

    def writeLog(self, message, maskName):
        self.date.setToNow()
        dateSring = self.date.getDateTime()
        self.lines += 1
        self.logFile.write(f"{dateSring} - {maskName} - {message}\n")
        if self.lines >= self.maxLines:
            self.logFile.close()
            self.createLogFile()

    def setMask(self, mask):
        self.mask = mask

    def getMask(self):
        return self.mask

    def setValueInMask(self, mask):
        self.mask = self.mask | mask

    def unsetValueInMask(self, mask):
        self.mask = self.mask & ~mask

    def flush(self):
        self.logFile.flush()

    def restartFile(self):
        self.logFile.close()
        self.lines = 0
        self.createLogFile()

    def getLogFilePath(self):
        return self.logFilePath

    def close(self):
        self.logFile.close()


log = Logger()
