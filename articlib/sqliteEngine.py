import sqlite3
import logging


log = logging.getLogger()


class sqliteEngine:
    def __init__(self, dbPath):
        self.con = sqlite3.connect(dbPath)
        self.cursor = self.con.cursor()

    def executeCommand(self, command):
        log.debug(f"Executing command: {command}")
        self.cursor.execute(command)

    def createTable(self, name, columns):
        self.executeCommand(f"CREATE TABLE {name} ({columns});")

    def addColumn(self, table, column):
        self.executeCommand(f"ALTER TABLE {table} ADD COLUMN {column};")

    def deleteColumn(self, table, column):
        self.executeCommand(f"ALTER TABLE {table} DROP COLUMN {column}")

    def addEntry(self, table, columns, values):
        self.executeCommand(f"INSERT INTO {table} ({columns}) VALUES ({values});")

    def updateEntry(self, table, columns, values, condition):
        self.executeCommand(
            f'UPDATE {table} SET {columns} = "{values}" WHERE {condition};'
        )

    def deleteEntry(self, table, condition):
        self.executeCommand(f"DELETE FROM {table} WHERE {condition};")

    def readEntry(self, table, columns):
        self.executeCommand(f"SELECT {columns} FROM {table};")
        result = self.cursor.fetchall()
        log.debug(f"Read entry: {result}")
        return result

    def readNumberOfEntries(self, table):
        self.executeCommand(f"SELECT COUNT(*) FROM {table};")
        result = self.cursor.fetchall()
        log.debug(f"Read number of entries: {result}")
        return result[0][0]

    def readEntryFiltered(self, table, columns, filter):
        self.executeCommand(f"SELECT {columns} FROM {table} WHERE {filter};")
        result = self.cursor.fetchall()
        log.debug(f"Read entry: {result}")
        return result

    def entryExistsOnTable(self, table, condition):
        self.executeCommand(f"SELECT * FROM {table} WHERE {condition};")
        entry = self.cursor.fetchall()
        if len(entry) != 0:
            return True
        else:
            return False

    def deleteEntryFromTable(self, table, condition):
        self.executeCommand(f"DELETE FROM {table} WHERE {condition};")

    def commit(self):
        self.con.commit()

    def commitClose(self):
        self.commit()
        self.con.close()
