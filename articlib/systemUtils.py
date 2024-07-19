import subprocess
import datetime

def executeCommand(command):
    result = subprocess.run(command)
    return result.returncode

class command:
    def __init__(self, command, run=True, capture=True, timeout=-1):
        self.command = command
        self.capture = capture
        self.timeout = timeout
        if run:
            self.run
    
    def run(self):
        if self.timeout > 0:
            self.process = subprocess.run(command, capture_output=self.capture, timeout=self.timeout)
        else:
            self.runWithoutTimeout
            

    def runWithoutTimeout(self):
        self.process = subprocess.run(command, capture_output=self.capture)
    
    def stdout(self):
        return self.process.stdout
    
    def stderr(self):
        return self.process.stderr



    
