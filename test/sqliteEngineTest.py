from articlib.testEngine import test
from articlib.sqliteEngine import sqliteEngine
import articlib.articFileUtils as fileUtils

fileUtils.deleteFile("test.sqlite") if fileUtils.fileExists("test.sqlite") else None
sqliteEngine1 = sqliteEngine("test.sqlite")

def runTest():
    print("Starting test for sqlite engine")
    runScenario1()
    runScenario2()
    sqliteEngine1.commitClose()
    fileUtils.deleteFile("test.sqlite")
    print("Finished test for sqlite engine")
    
def runScenario1():
    test.newScenario("Create table, add entry, read entry, delete entry, update entry")
    test11()
    test12()
    test13()
    test14()
    test15()
    test.endScenario("Create table, add entry, read entry, delete entry, update entry")
    
def runScenario2():
    test.newScenario("Add column to table and count entries")
    test21()
    test22()
    test.endScenario("Add column to table and count entries")
    
def test11():
    sqliteEngine1.createTable("test", "id INTEGER PRIMARY KEY, name TEXT, value TEXT")
    sqliteEngine1.addEntry("test", "name, value", "'testName', 'testValue'")
    result = sqliteEngine1.readEntry("test", "name, value")
    test.testIfEqual([('testName', 'testValue')], result, "Checking entry added")
    
def test12():
    sqliteEngine1.updateEntry("test", "name", "'testName2'", "id = 1")
    result = sqliteEngine1.readEntry("test", "name, value")
    test.testIfEqual([('testName2', 'testValue')], result, "Checking entry updated")
    
def test13():
    sqliteEngine1.deleteEntry("test", "id = 1")
    result = sqliteEngine1.readEntry("test", "name, value")
    test.testIfEqual([], result, "Checking entry deleted")
    
def test14():
    sqliteEngine1.addEntry("test", "name, value", "'testName', 'testValue'")
    sqliteEngine1.addEntry("test", "name, value", "'testName2', 'testValue2'")
    result = sqliteEngine1.readEntryFiltered("test", "name, value", "id = 2")
    test.testIfEqual([('testName2', 'testValue2')], result, "Checking entry filtered")

def test15():
    result = sqliteEngine1.entryExistsOnTable("test", "id = 2")
    test.testIfEqual(True, result, "Checking entry exists")
    result = sqliteEngine1.entryExistsOnTable("test", "id = 3")
    test.testIfEqual(False, result, "Checking entry doesn't exist")
    sqliteEngine1.deleteEntry("test", "id = 1")
    sqliteEngine1.deleteEntry("test", "id = 2")
    
def test21():
    sqliteEngine1.addColumn("test", "testColumn TEXT")
    sqliteEngine1.addEntry("test", "name, value, testColumn", "'testName', 'testValue', 'testValue'")
    sqliteEngine1.addEntry("test", "name, value, testColumn", "'testName2', 'testValue2', 'testValue2'")
    result = sqliteEngine1.readEntry("test", "testColumn")
    test.testIfEqual([('testValue',), ('testValue2',)], result, "Checking column added")
    
def test22():
    result = sqliteEngine1.readNumberOfEntries("test")
    test.testIfEqual(2, result, "Checking number of entries")
    
if __name__ == "__main__":
    runTest()
    test.printResults()