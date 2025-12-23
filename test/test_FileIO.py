import logging
import pytest
import articlib.articFileUtils as AFU


log = logging.getLogger()


@pytest.fixture
def FilePointer() -> AFU.FileIO:
    log.info("=== Create file for test in fixture ===")
    FP = AFU.FileIO("testFile", readIt=False)
    FP.addLine("line1")
    FP.addLine("line2")
    return FP


def test_add_line(FilePointer):
    FilePointer.addLine("line3")
    assert FilePointer.lines == ["line1", "line2", "line3"]


def test_remove_line(FilePointer):
    FilePointer.removeLine(0)
    assert FilePointer.lines == ["line2"]


def test_remove_last_line(FilePointer):
    FilePointer.removeLastLine()
    assert FilePointer.lines == ["line1"]


def test_line_count(FilePointer):
    assert FilePointer.lineCount() == 2
    FilePointer.addLine("line2")
    assert FilePointer.lineCount() == 3
    FilePointer.removeLastLine()
    FilePointer.removeLastLine()
    assert FilePointer.lineCount() == 1


def test_modify_line(FilePointer):
    FilePointer.modifyLine(0, "lineModified")
    assert FilePointer.lines == ["lineModified", "line2"]


def test_find_line(FilePointer):
    assert FilePointer.findLine("1") == [0]
    assert FilePointer.findLine("line") == [0, 1]


def test_find_replace(FilePointer):
    FilePointer.findAndReplace("line", "fila")
    assert FilePointer.lines == ["fila1", "fila2"]


def test_write_read_from_file(FilePointer):
    FilePointer.writeFile()
    FilePointer.addLine("line3")
    FilePointer.readFile()
    assert FilePointer.lines == ["line1", "line2"]


def test_append_to_file(FilePointer):
    FilePointer.writeFile()
    FilePointer.appendToFile()
    FilePointer.readFile()
    assert FilePointer.lines == ["line1", "line2", "line1", "line2"]


def test_read_at_init(FilePointer):
    FilePointer.writeFile()
    newFile = AFU.FileIO("testFile", readIt=True)
    assert FilePointer.lines == newFile.lines
    log.info("Repeat with default value")
    newFile1 = AFU.FileIO("testFile")
    assert newFile1.lines == []
