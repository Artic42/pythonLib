import os

def deleteFile(path):
    os.remove(path)
    
def createFile(path):
    file = open (path, "r")
    file.close()

def fileExists(path):
    return os.path.isfile(path)

def getFilesInDirectory(path):
    return os.listdir(path)
    
def deleteDirectory(path):
    os.rmdir(path)
    
def createDirectory(path):
    os.makedirs(path, exist_ok=True)

class FileIO:
    def __init__(self, path, readIt = False):
        self.path = path
        if readIt:
            self.readFile()
    
    def readFile(self):
        filePointer = open (self.path, "r")
        self.lines = filePointer.readlines()
        filePointer.close()
    
    def writeFile(self):
        filePointer = open (self.path, "w")
        for line in self.lines:
            filePointer.write(line + "\n")
        filePointer.close()
    
    def appendToFile(self):
        filePointer = open (self.path, "a")
        for line in self.lines:
            filePointer.write(line + "\n")
        filePointer.close()
    
    def addLine(self, line):
        self.lines.append(line)
        
    def lineCount(self):
        return len(self.lines)