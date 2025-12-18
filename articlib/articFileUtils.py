import os
import shutil
import logging
from articlib import logUtils as LU


logObj = logging.getLogger()


def deleteFile(path: str) -> None:
    logObj.debug(f"Delete the file on path {path}")
    os.remove(path)


def createFile(path: str) -> None:
    logObj.debug(f"Create file on path {path}")
    file = open(path, "w")
    file.close()


def copyFile(source: str, destination: str) -> None:
    logObj.debug(f"Copy file from {source} to {destination}")
    shutil.copy(source, destination)


def fileExists(path: str) -> bool:
    return os.path.isfile(path)


def getFilesInDirectory(path: str) -> list[str]:
    return os.listdir(path)


def deleteDirectory(path: str) -> None:
    logObj.debug(f"Delete directory on {path}")
    os.rmdir(path)


def deleteDirectoryTree(path: str) -> None:
    logObj.debug(f"Remove entire directory tree in {path}")
    shutil.rmtree(path)


def createDirectory(path: str) -> None:
    logObj.debug(f"Create directory on {path}")
    os.makedirs(path, exist_ok=True)


def directoryExists(path: str) -> bool:
    return os.path.isdir(path)


class FileIO:
    def __init__(self, path: str, readIt: bool = False, log: bool = True) -> None:
        self.log = log
        self.path = path
        if self.log is True:
            logObj.debug(f"Create FileIO object with path {self.path}")
        if readIt is True:
            logObj.info(f"Reading content in path {self.path}")
            self.readFile()
        else:
            logObj.info("Load file as empty without reading")
            self.lines = []

    def readFile(self) -> None:
        filePointer = open(self.path, "r")
        if self.log is True:
            logObj.info(f"Read file in {self.path}")
            LU.logFile(self.path, debugFlag=True)
        self.lines = filePointer.readlines()
        self.lines = [line[:-1] for line in self.lines]
        filePointer.close()

    def writeFile(self) -> None:
        filePointer = open(self.path, "w")
        for line in self.lines:
            filePointer.write(line + "\n")
        if self.log is True:
            logObj.info(f"Write file in {self.path}")
            LU.logFile(self.path, debugFlag=True)

        filePointer.close()

    def appendToFile(self) -> None:
        filePointer = open(self.path, "a")
        for line in self.lines:
            filePointer.write(line + "\n")
        if self.log is True:
            logObj.info(f"Append to file in {self.path}")
            LU.logFile(self.path, debugFlag=True)
        filePointer.close()

    def addLine(self, line: str) -> None:
        if self.log is True:
            logObj.info(f"Addline: {line}")
        self.lines.append(line)

    def modifyLine(self, lineNumber: int, line: str) -> None:
        if self.log is True:
            logObj.info(f"Modify line {lineNumber} to {line}")
        self.lines[lineNumber] = line

    def removeLine(self, lineNumber: int) -> None:
        if self.log is True:
            logObj.info(f"Remove line {lineNumber}")
            logObj.debug(f"Removed content is {self.lines[lineNumber]}")
        del self.lines[lineNumber]

    def removeLastLine(self) -> None:
        if self.log is True:
            logObj.info("Remove last line")
            logObj.debug(f"Removed content is {self.lines[-1]}")
        del self.lines[-1]

    def findLine(self, text: str) -> list[str]:
        result = []
        for i in range(len(self.lines)):
            if text in self.lines[i]:
                result.append(i)
        return result

    def findAndReplace(self, find: str, replace: str) -> None:
        if self.log is True:
            logObj.info(f"Find {find} and replace it with {replace}")
        for i in range(len(self.lines)):
            self.lines[i] = self.lines[i].replace(find, replace)

    def lineCount(self) -> int:
        return len(self.lines)
