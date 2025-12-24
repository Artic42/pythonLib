import sqlite3
import logging
from typing import Any


log = logging.getLogger()


class sqliteEngine:
    def __init__(self, dbPath: str):
        self.con = sqlite3.connect(dbPath)
        self.cursor = self.con.cursor()

    def executeCommand(self, command: str) -> None:
        log.debug(f"Executing command: {command}")
        self.cursor.execute(command)

    def createTable(self, name: str, columns: str) -> None:
        self.executeCommand(f"CREATE TABLE {name} ({columns});")

    def addColumn(self, table: str, column: str) -> None:
        self.executeCommand(f"ALTER TABLE {table} ADD COLUMN {column};")

    def deleteColumn(self, table: str, column: str) -> None:
        self.executeCommand(f"ALTER TABLE {table} DROP COLUMN {column}")

    def addEntry(self, table: str, columns: str, values: str) -> None:
        self.executeCommand(f"INSERT INTO {table} ({columns}) VALUES ({values});")

    def updateEntry(self, table: str, columns: str, values: str, condition: str) -> None:
        self.executeCommand(
            f'UPDATE {table} SET {columns} = "{values}" WHERE {condition};'
        )

    def deleteEntry(self, table: str, condition: str) -> None:
        self.executeCommand(f"DELETE FROM {table} WHERE {condition};")

    def readEntry(self, table: str, columns: str) -> list[Any]:
        self.executeCommand(f"SELECT {columns} FROM {table};")
        result = self.cursor.fetchall()
        log.debug(f"Read entry: {result}")
        return result

    def readNumberOfEntries(self, table: str) -> Any:
        self.executeCommand(f"SELECT COUNT(*) FROM {table};")
        result = self.cursor.fetchall()
        log.debug(f"Read number of entries: {result}")
        return result[0][0]

    def readEntryFiltered(self, table: str, columns: str, filter: str) -> list[Any]:
        self.executeCommand(f"SELECT {columns} FROM {table} WHERE {filter};")
        result = self.cursor.fetchall()
        log.debug(f"Read entry: {result}")
        return result

    def entryExistsOnTable(self, table: str, condition: str) -> bool:
        self.executeCommand(f"SELECT * FROM {table} WHERE {condition};")
        entry = self.cursor.fetchall()
        if len(entry) != 0:
            return True
        else:
            return False

    def deleteEntryFromTable(self, table: str, condition: str) -> None:
        self.executeCommand(f"DELETE FROM {table} WHERE {condition};")

    def commit(self) -> None:
        self.con.commit()

    def commitClose(self) -> None:
        self.commit()
        self.con.close()
