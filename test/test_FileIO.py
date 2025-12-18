import logging
import pytest
import articlib.articFileUtils as AFU
from articlib import logUtils as LU


log = logging.getLogger()


@pytest.fixture
def FilePointer() -> AFU.FileIO:
    log.info("=== Create file for test in fixture ===")
    FP = AFU.FileIO("testFile", readIt=False)
    FP.addLine("line1")
    FP.addLine("line2")
    return FP


def test_add_line(FilePointer):
    LU.logTestStart("Test add line")
    FilePointer.addLine("line3")
    assert FilePointer.lines == ["line1", "line2", "line3"]
    LU.logTestEnd()


def test_remove_line(FilePointer):
    LU.logTestStart("Test remove line")
    FilePointer.removeLine(0)
    assert FilePointer.lines == ["line2"]
    LU.logTestEnd()


def test_remove_last_line(FilePointer):
    LU.logTestStart("Test remove last line")
    FilePointer.removeLastLine()
    assert FilePointer.lines == ["line1"]
    LU.logTestEnd()


def test_line_count(FilePointer):
    LU.logTestStart("Test count line method")
    assert FilePointer.lineCount() == 2
    FilePointer.addLine("line2")
    assert FilePointer.lineCount() == 3
    FilePointer.removeLastLine()
    FilePointer.removeLastLine()
    assert FilePointer.lineCount() == 1
    LU.logTestEnd()


def test_modify_line(FilePointer):
    LU.logTestStart("Test line modify method")
    FilePointer.modifyLine(0, "lineModified")
    assert FilePointer.lines == ["lineModified", "line2"]
    LU.logTestEnd()


def test_find_line(FilePointer):
    LU.logTestStart("Test find lines method")
    assert FilePointer.findLine("1") == [0]
    assert FilePointer.findLine("line") == [0, 1]
    LU.logTestEnd()


def test_find_replace(FilePointer):
    LU.logTestStart("Test find and replace method")
    FilePointer.findAndReplace("line", "fila")
    assert FilePointer.lines == ["fila1", "fila2"]
    LU.logTestEnd()


def test_write_read_from_file(FilePointer):
    LU.logTestStart("Test read and write from a file")
    FilePointer.writeFile()
    FilePointer.addLine("line3")
    FilePointer.readFile()
    assert FilePointer.lines == ["line1", "line2"]
    LU.logTestEnd()


def test_append_to_file(FilePointer):
    LU.logTestStart("Test append to file")
    FilePointer.writeFile()
    FilePointer.appendToFile()
    FilePointer.readFile()
    assert FilePointer.lines == ["line1", "line2", "line1", "line2"]
    LU.logTestEnd()


def test_read_at_init(FilePointer):
    LU.logTestStart("Test read at instance initialization")
    FilePointer.writeFile()
    newFile = AFU.FileIO("testFile", readIt=True)
    assert FilePointer.lines == newFile.lines
    log.info("Repeat with default value")
    newFile1 = AFU.FileIO("testFile")
    assert newFile1.lines == []
    LU.logTestEnd()
