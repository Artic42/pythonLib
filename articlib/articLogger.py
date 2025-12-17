import articlib.dateTime as dateTime
import os
from articlib.consoleUtils import (
    printGreen,
    printYellow,
    printRed,
)

if __name__ == "__main__":
    pass


class Logger:
    __instance = None

    INFO_MASK = 0b00000001
    WARN_MASK = 0b00000010
    ERROR_MASK = 0b00000100
    COMMS_SEND_MASK = 0b00001000
    COMMS_RECV_MASK = 0b00010000
    HERMES_MASK = 0b00100000
    COMMS_MASK = 0b00011000
    DEBUG_MASK = 0b01000000
    DEFAULT_MASK = INFO_MASK | COMMS_MASK | ERROR_MASK | HERMES_MASK

    @staticmethod
    def getInstance():
        """Static access method to get the singleton instance"""
        if Logger.__instance is None:
            Logger.__instance = Logger()
        return Logger.__instance

    def __init__(self):
        self.init = False
        self.logName = ""
        self.maxLines = 0
        self.lines = 0
        self.logPath = ""
        self.mask = 0b0

    def initialize(
        self,
        logName: str,
        maxLines: int = 1000,
        logPath: str = "logs",
        mask: int = DEFAULT_MASK,
        consoleOutput: bool = True,
    ):
        self.consoleOutput = consoleOutput
        self.init = True
        self.logName = logName
        self.maxLines = maxLines
        self.lines = 0
        self.logPath = logPath
        self.mask = mask
        self.date = dateTime.createDate(dateTime.YYYYMMDD)
        self.createLogFile()

    def createLogFile(self) -> None:
        self.date.setToNow()
        dateString = self.date.getDateTimePathFormat()
        os.makedirs(self.logPath, exist_ok=True)
        self.logFilePath = f"{self.logPath}/{self.logName}_{dateString}.log"
        if os.path.isfile(self.logFilePath):
            self.logFile = open(self.logFilePath, "a")
        else:
            self.logFile = open(self.logFilePath, "w")
            self.logFile.write(
                (
                    f"Log file created at"
                    f" {self.date.getDateTime()}"
                    f"with name {self.logName}\n"
                )
            )
            self.lines = 0

    def addEntry(
        self, message: str, mask: int = INFO_MASK, consoleOutput: bool = True
    ) -> None:
        if not self.init:
            return
        maskName = self.getMaskName(mask)
        if mask & self.mask:
            self.writeLog(message, maskName, consoleOutput)

    def getMaskName(self, mask: int) -> str:
        """Returns the name of the mask based on its value."""
        switcher = {
            Logger.INFO_MASK: "INFO",
            Logger.WARN_MASK: "WARN",
            Logger.ERROR_MASK: "ERROR",
            Logger.COMMS_SEND_MASK: "COMMS_SEND",
            Logger.COMMS_RECV_MASK: "COMMS_RECV",
            Logger.HERMES_MASK: "HERMES",
            Logger.DEBUG_MASK: "DEBUG",
            Logger.DEFAULT_MASK: "DEFAULT",
        }
        return switcher.get(mask, "UNKNOWN")

    def writeLog(self, message: str, maskName: str, consoleOutput: bool = True) -> None:
        self.date.setToNow()
        dateString = self.date.getDateTime()
        self.lines += 1
        self.logFile.write(f"{dateString} - {maskName} - {message}\n")
        if consoleOutput:
            self.outputToConsole(f"{dateString} - {maskName} - {message}", maskName)
        if self.lines >= self.maxLines:
            self.logFile.close()
            self.createLogFile()

    def outputToConsole(self, message: str, maskName: str) -> None:
        if maskName == "WARN":
            printYellow(message)
        elif maskName == "ERROR":
            printRed(message)
        else:
            printGreen(message)

    def setMask(self, mask: int) -> None:
        self.mask = mask

    def getMask(self) -> int:
        return self.mask

    def setValueInMask(self, mask: int) -> None:
        self.mask = self.mask | mask

    def unsetValueInMask(self, mask: int) -> None:
        self.mask = self.mask & ~mask

    def flush(self) -> None:
        self.logFile.flush()

    def restartFile(self) -> None:
        self.logFile.close()
        self.lines = 0
        self.createLogFile()

    def getLogFilePath(self) -> str:
        return self.logFilePath

    def close(self) -> None:
        self.logFile.close()
