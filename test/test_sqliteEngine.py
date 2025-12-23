import logging
import pytest
from articlib.sqliteEngine import sqliteEngine
import articlib.articFileUtils as fileUtils


log = logging.getLogger()


@pytest.fixture
def sqlDB() -> sqliteEngine:
    if fileUtils.fileExists("test.sqlite"):
        fileUtils.deleteFile("test.sqlite")  # Delete file if it exists
    DB = sqliteEngine("test.sqlite")
    DB.createTable("test", "id INTEGER PRIMARY KEY, name TEXT, value TEXT")
    return DB


def test_add_update_delete(sqlDB):
    sqlDB.addEntry("test", "name, value", "'testName', 'testValue'")
    result = sqlDB.readEntry("test", "name, value")
    assert [("testName", "testValue")] == result
    log.info("Entry created")

    sqlDB.updateEntry("test", "name", "'testName2'", "id = 1")
    result = sqlDB.readEntry("test", "name, value")
    assert [("'testName2'", "testValue")] == result
    log.info("Entry updated")

    sqlDB.deleteEntry("test", "id = 1")
    result = sqlDB.readEntry("test", "name, value")
    assert [] == result


def test_read_filtered_entry(sqlDB):
    sqlDB.addEntry("test", "name, value", "'testName', 'testValue'")
    sqlDB.addEntry("test", "name, value", "'testName2', 'testValue2'")
    result = sqlDB.readEntryFiltered("test", "name, value", "id = 2")
    assert [("testName2", "testValue2")] == result


def test_entry_exists_on_table(sqlDB):
    sqlDB.addEntry("test", "name, value", "'testName', 'testValue'")
    sqlDB.addEntry("test", "name, value", "'testName2', 'testValue2'")
    result = sqlDB.entryExistsOnTable("test", "id = 2")
    assert result is True
    result = sqlDB.entryExistsOnTable("test", "id = 3")
    assert result is False


def test_add_column(sqlDB):
    sqlDB.addColumn("test", "testColumn TEXT")
    sqlDB.addEntry(
        "test",
        "name, value, testColumn",
        "'testName', 'testValue', 'testValue'"
    )
    sqlDB.addEntry(
        "test",
        "name, value, testColumn",
        "'testName2', 'testValue2', 'testValue2'"
    )
    result = sqlDB.readEntry("test", "testColumn")
    assert [("testValue",), ("testValue2",)] == result


def test_read_number_entries(sqlDB):
    sqlDB.addEntry("test", "name, value", "'testName', 'testValue'")
    sqlDB.addEntry("test", "name, value", "'testName2', 'testValue2'")
    result = sqlDB.readNumberOfEntries("test")
    assert result == 2
