import logging
import articlib.articFileUtils as AFU


log = logging.getLogger()
TEST_DIR = "testDir"
TEST_FILE = "testFile"
TEST_FILE_COPY = "test/files/testFile"


def test_directory_manipulation():
    AFU.createDirectory(TEST_DIR)
    assert AFU.directoryExists(TEST_DIR)
    AFU.deleteDirectory(TEST_DIR)
    assert AFU.directoryExists(TEST_DIR) is False

def test_file_manipulation():
    AFU.createFile(TEST_FILE)
    assert AFU.fileExists(TEST_FILE)
    AFU.deleteFile(TEST_FILE)
    assert AFU.fileExists(TEST_FILE) is False


def test_copy_file():
    AFU.copyFile(TEST_FILE_COPY, TEST_FILE)
    file1 = open(TEST_FILE_COPY, "r")
    file2 = open(TEST_FILE, "r")
    assert file1.readlines() == file2.readlines()
    AFU.deleteFile(TEST_FILE)


def test_get_files_in_dir():
    AFU.createDirectory(TEST_DIR)
    AFU.createFile(TEST_DIR + "/file1")
    AFU.createFile(TEST_DIR + "/file2")
    result: list[str] = AFU.getFilesInDirectory(TEST_DIR)
    assert result == ["file1", "file2"]
    AFU.deleteDirectoryTree(TEST_DIR)
    assert AFU.directoryExists(TEST_DIR) is False
