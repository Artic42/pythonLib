from testEngine import test
from sqliteEngine import sqliteEngine
import articFileUtils as fileUtils

sqliteEngine1 = sqliteEngine("test.db")

def runTest():
    print("Starting test for sqlite engine")
    runScenario1()
    sqliteEngine1.commitClose()
    fileUtils.deleteFile("test.db")
    print("Finished test for sqlite engine")
    
def runScenario1():
    test.newScenario("Create table, add entry, read entry, delete entry, update entry")
    test11()
    test12()
    test13()
    test14()
    test15()
    test.endScenario("Create table, add entry, read entry, delete entry, update entry")
    
def test11():
    sqliteEngine1.createTable("test", "id INTEGER PRIMARY KEY, name TEXT, value TEXT")
    sqliteEngine1.addEntry("test", "name, value", "'testName', 'testValue'")
    result = sqliteEngine1.readEntry("name, value", "test")
    test.testIfEqual([('testName', 'testValue')], result, "Checking entry added")
    
def test12():
    sqliteEngine1.updateEntry("test", "name", "'testName2'", "id = 1")
    result = sqliteEngine1.readEntry("name, value", "test")
    test.testIfEqual([('testName2', 'testValue')], result, "Checking entry updated")
    
def test13():
    sqliteEngine1.deleteEntry("test", "id = 1")
    result = sqliteEngine1.readEntry("name, value", "test")
    test.testIfEqual([], result, "Checking entry deleted")
    
def test14():
    sqliteEngine1.addColumn("test", "newColumn TEXT")
    sqliteEngine1.addEntry("test", "name, value, newColumn", "'testName', 'testValue', 'testNewColumn'")
    result = sqliteEngine1.readEntry("name, value, newColumn", "test")
    test.testIfEqual([('testName', 'testValue', 'testNewColumn')], result, "Checking entry added with new column")
    
def test15():
    sqliteEngine1.deleteColumn("test", "newColumn")
    result = sqliteEngine1.readEntry("newColumn", "test")
    test.testIfEqual([], result, "Checking column deleted")
    
    
if __name__ == "__main__":
    runTest()
    test.printResults()