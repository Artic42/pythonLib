

from articlib.systemUtils import executeCommand
import articlib.systemUtils as systemUtils

result = executeCommand ("ls")

print(result)
print(result.returncode)
print(systemUtils.exitCode)