

from systemUtils import executeCommand
import systemUtils

result = executeCommand ("ls")

print(result)
print(result.returncode)
print(systemUtils.exitCode)