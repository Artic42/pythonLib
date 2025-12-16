import os
import shutil


def deleteFile(path: str) -> None:
    os.remove(path)


def createFile(path: str) -> None:
    file = open(path, "r")
    file.close()


def copyFile(source: str, destination: str) -> None:
    shutil.copy(source, destination)


def fileExists(path: str) -> bool:
    return os.path.isfile(path)


def getFilesInDirectory(path: str) -> list[str]:
    return os.listdir(path)


def deleteDirectory(path: str) -> None:
    os.rmdir(path)


def createDirectory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


class FileIO:
    def __init__(self, path: str, readIt: bool = False) -> None:
        self.path = path
        if readIt:
            self.readFile()
        else:
            self.lines = []

    def readFile(self) -> None:
        filePointer = open(self.path, "r")
        self.lines = filePointer.readlines()
        self.lines = [line[:-1] for line in self.lines]
        filePointer.close()

    def writeFile(self) -> None:
        filePointer = open(self.path, "w")
        for line in self.lines:
            filePointer.write(line + "\n")
        filePointer.close()

    def appendToFile(self) -> None:
        filePointer = open(self.path, "a")
        for line in self.lines:
            filePointer.write(line + "\n")
        filePointer.close()

    def addLine(self, line: str) -> None:
        self.lines.append(line)

    def modifyLine(self, lineNumber: int, line: str) -> None:
        self.lines[lineNumber] = line

    def removeLine(self, lineNumber: int) -> None:
        del self.lines[lineNumber]

    def removeLastLine(self) -> None:
        del self.lines[-1]

    def findLine(self, text: str) -> list[str]:
        result = []
        for i in range(len(self.lines)):
            if text in self.lines[i]:
                result.append(i)
        return result

    def findAndReplace(self, find: str, replace: str) -> None:
        for i in range(len(self.lines)):
            self.lines[i] = self.lines[i].replace(find, replace)

    def lineCount(self) -> int:
        return len(self.lines)
