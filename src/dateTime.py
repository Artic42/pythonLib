from datetime import datetime

YYYYMMDD = 1
DDMMYYYY = 2
MMDDYYYY = 3

class createDate:
    def __init__(self, mode):
        self.mode = mode
    
    def setToNow(self):
        date = datetime.now()
        self.year = int(date.year)
        self.month = int(date.month)
        self.day = int(date.day)
        self.hour = int(date.hour)
        self.minute = int(date.minute)
        self.second = int(date.second)
        self.calculateStringDate()
        self.calculateStringTime()
    
    def setTo(self, year, month, day, hour, minute, second):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.calculateStringDate()
        self.calculateStringTime()
        
    def setToString(self, string):
        string = string.split(" ")
        date = string[0]
        time = string[1]
        self.dateString = date
        self.timeString = time
        self.calculateDate()
        self.calculateTime()
    
    def calculateDate(self):
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
        
    def calculateTime(self):
        self.hour = int(self.timeString[0:2])
        self.minute = int(self.timeString[3:5])
        self.second = int(self.timeString[6:8])
        
    def calculateStringDate(self):
        if self.mode == YYYYMMDD:
            self.dateString = str(self.year) + "/" + str(self.month) + "/" + str(self.day)
        elif self.mode == DDMMYYYY:
            self.dateString = str(self.day) + "/" + str(self.month) + "/" + str(self.year)
        elif self.mode == MMDDYYYY:
            self.dateString = str(self.month) + "/" + str(self.day) + "/" + str(self.year)
        else:
            raise ValueError("Invalid mode")
    
    def calculateStringTime(self):
        self.timeString = str(self.hour) + ":" + str(self.minute) + ":" + str(self.second)
        
    def setMode(self, mode):
        self.mode = mode
        self.calculateStringDate()
        
    ## Output values
    def getDateTimePathFomat(self):
        string1 = f"{self.year}{self.month}{self.day}"
        string2 = f"{self.hour}{self.minute}{self.second}"
        return f"{string1}_{string2}"
    
    def getDate(self):
        return self.dateString
    
    def getTime(self):
        return self.timeString
    
    def getDateTime(self):
        return self.dateString + " " + self.timeString
    
    def getYear(self):
        return self.year
    
    def getMonth(self):
        return self.month
    
    def getDay(self):
        return self.day
    
    def getHour(self):
        return self.hour
    
    def getMinute(self):
        return self.minute
    
    def getSecond(self):
        return self.second
    
    def getMode(self):
        return self.mode
    
