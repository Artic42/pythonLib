import os



def deleteFile(path):
    os.remove(path)

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