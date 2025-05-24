from datetime import datetime

YYYYMMDD = 1
DDMMYYYY = 2
MMDDYYYY = 3


class createDate:
    def __init__(self, mode) -> None:
        self.mode = mode

    def setToNow(self) -> None:
        date = datetime.now()
        self.year = int(date.year)
        self.month = int(date.month)
        self.day = int(date.day)
        self.hour = int(date.hour)
        self.minute = int(date.minute)
        self.second = int(date.second)
        self.calculateStringDate()
        self.calculateStringTime()

    def setTo(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int
    ) -> None:
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.calculateStringDate()
        self.calculateStringTime()

    def setToString(self, string: str) -> None:
        string = string.split(" ")
        date = string[0]
        time = string[1]
        self.dateString = date
        self.timeString = time
        self.calculateDate()
        self.calculateTime()

    def calculateDate(self) -> None:
        if self.mode == YYYYMMDD:
            self.year = int(self.dateString[0:4])
            self.month = int(self.dateString[5:7])
            self.day = int(self.dateString[8:10])
        elif self.mode == DDMMYYYY:
            self.day = int(self.dateString[0:2])
            self.month = int(self.dateString[3:5])
            self.year = int(self.dateString[6:10])
        elif self.mode == MMDDYYYY:
            self.month = int(self.dateString[0:2])
            self.day = int(self.dateString[3:5])
            self.year = int(self.dateString[6:10])
        else:
            raise ValueError("Invalid mode")

    def calculateTime(self) -> None:
        self.hour = int(self.timeString[0:2])
        self.minute = int(self.timeString[3:5])
        self.second = int(self.timeString[6:8])

    def calculateStringDate(self) -> None:
        if self.mode == YYYYMMDD:
            self.dateString = str(self.year) + "/"
            self.dateString += str(self.month).zfill(2) + "/"
            self.dateString += str(self.day).zfill(2)
        elif self.mode == DDMMYYYY:
            self.dateString = str(self.day).zfill(2) + "/"
            self.dateString += str(self.month).zfill(2) + "/"
            self.dateString += str(self.year)
        elif self.mode == MMDDYYYY:
            self.dateString = str(self.month).zfill(2) + "/"
            self.dateString += str(self.day).zfill(2) + "/"
            self.dateString += str(self.year)
        else:
            raise ValueError("Invalid mode")

    def calculateStringTime(self) -> None:
        self.timeString = str(self.hour).zfill(2) + ":"
        self.timeString += str(self.minute).zfill(2) + ":"
        self.timeString += str(self.second).zfill(2)

    def setMode(self, mode: int) -> None:
        self.mode = mode
        self.calculateStringDate()

    # Output values
    def getDateTimePathFormat(self) -> str:
        if self.mode == YYYYMMDD:
            dateString = (
                str(self.year) + str(self.month).zfill(2) + str(self.day).zfill(2)
            )
        elif self.mode == DDMMYYYY:
            dateString = (
                str(self.day).zfill(2) + str(self.month).zfill(2) + str(self.year)
            )
        elif self.mode == MMDDYYYY:
            dateString = (
                str(self.month).zfill(2) + str(self.day).zfill(2) + str(self.year)
            )
        else:
            raise ValueError("Invalid mode")
        timeString = str(self.hour).zfill(2)
        timeString += str(self.minute).zfill(2)
        timeString += str(self.second).zfill(2)
        return f"{dateString}_{timeString}"

    def getDate(self) -> str:
        return self.dateString

    def getTime(self) -> str:
        return self.timeString

    def getDateTime(self) -> str:
        return self.dateString + " " + self.timeString

    def getYear(self) -> int:
        return self.year

    def getMonth(self) -> int:
        return self.month

    def getDay(self) -> int:
        return self.day

    def getHour(self) -> int:
        return self.hour

    def getMinute(self) -> int:
        return self.minute

    def getSecond(self) -> int:
        return self.second

    def getMode(self) -> int:
        return self.mode
