import articlib.dateTime as dateTime
from articlib.testEngine import testEngine
from articlib.articLogger import Logger

test = testEngine.getInstance()


def runTest():
    print("Starting test for dateTime")
    runScenario1()
    runScenario2()
    runScenario3()
    runScenario4()
    runScenario5()
    print("Finished test for dateTime")


def runScenario1():
    test.newScenario("Check setTo function")
    date = dateTime.createDate(dateTime.YYYYMMDD)
    date.setTo(2020, 10, 1, 10, 10, 10)
    test.testIfEqual(2020, date.year, "Checking year is 2020")
    test.testIfEqual(10, date.month, "Checking month is 10")
    test.testIfEqual(1, date.day, "Checking day is 1")
    test.testIfEqual(10, date.hour, "Checking hour is 10")
    test.testIfEqual(10, date.minute, "Checking minute is 10")
    test.testIfEqual(10, date.second, "Checking second is 10")
    test.endScenario("Check setTo function")


def runScenario2():
    test.newScenario("Check setToString function in mode YYYYMMDD")
    date = dateTime.createDate(dateTime.YYYYMMDD)
    date.setToString("2020/10/01 10:10:10")
    test.testIfEqual(2020, date.year, "Checking year is 2020")
    test.testIfEqual(10, date.month, "Checking month is 10")
    test.testIfEqual(1, date.day, "Checking day is 1")
    test.testIfEqual(10, date.hour, "Checking hour is 10")
    test.testIfEqual(10, date.minute, "Checking minute is 10")
    test.testIfEqual(10, date.second, "Checking second is 10")
    test.endScenario("Check setToString function in mode YYYYMMDD")


def runScenario3():
    test.newScenario("Check setToString function in mode DDMMYYYY")
    date = dateTime.createDate(dateTime.DDMMYYYY)
    date.setToString("01/10/2020 10:10:10")
    test.testIfEqual(2020, date.year, "Checking year is 2020")
    test.testIfEqual(10, date.month, "Checking month is 10")
    test.testIfEqual(1, date.day, "Checking day is 1")
    test.testIfEqual(10, date.hour, "Checking hour is 10")
    test.testIfEqual(10, date.minute, "Checking minute is 10")
    test.testIfEqual(10, date.second, "Checking second is 10")
    test.endScenario("Check setToString function in mode DDMMYYYY")


def runScenario4():
    test.newScenario("Check setToString function in mode MMDDYYYY")
    date = dateTime.createDate(dateTime.MMDDYYYY)
    date.setToString("10/01/2020 10:10:10")
    test.testIfEqual(2020, date.year, "Checking year is 2020")
    test.testIfEqual(10, date.month, "Checking month is 10")
    test.testIfEqual(1, date.day, "Checking day is 1")
    test.testIfEqual(10, date.hour, "Checking hour is 10")
    test.testIfEqual(10, date.minute, "Checking minute is 10")
    test.testIfEqual(10, date.second, "Checking second is 10")
    test.endScenario("Check setToString function in mode MMDDYYYY")


def runScenario5():
    test.newScenario("Date time string output")
    test51()
    test52()
    test53()
    test54()
    test55()
    test56()
    test.endScenario("Date time string output")


def test51():
    date = dateTime.createDate(dateTime.YYYYMMDD)
    dateTimeString = "2020/10/01 10:10:10"
    date.setToString(dateTimeString)
    test.testIfEqual(
        dateTimeString,
        date.getDateTime(),
        "Checking outputted in string format mode YYYYMMDD",
    )


def test52():
    date = dateTime.createDate(dateTime.DDMMYYYY)
    dateTimeString = "01/10/2020 10:10:10"
    date.setToString(dateTimeString)
    test.testIfEqual(
        dateTimeString,
        date.getDateTime(),
        "Checking outputted in string format mode DDMMYYYY",
    )


def test53():
    date = dateTime.createDate(dateTime.MMDDYYYY)
    dateTimeString = "10/01/2020 10:10:10"
    date.setToString(dateTimeString)
    test.testIfEqual(
        dateTimeString,
        date.getDateTime(),
        "Checking outputted in string format mode MMDDYYYY",
    )


def test54():
    date = dateTime.createDate(dateTime.YYYYMMDD)
    dateTimeString = "2020/10/01 10:10:10"
    date.setToString(dateTimeString)
    test.testIfEqual(
        "20201001_101010",
        date.getDateTimePathFormat(),
        "Checking outputted in path format on mode YYYYMMDDq",
    )


def test55():
    date = dateTime.createDate(dateTime.DDMMYYYY)
    dateTimeString = "01/10/2020 10:10:10"
    date.setToString(dateTimeString)
    test.testIfEqual(
        "01102020_101010",
        date.getDateTimePathFormat(),
        "Checking outputted in path format on mode DDMMYYYY",
    )


def test56():
    date = dateTime.createDate(dateTime.MMDDYYYY)
    dateTimeString = "10/01/2020 10:10:10"
    date.setToString(dateTimeString)
    test.testIfEqual(
        "10012020_101010",
        date.getDateTimePathFormat(),
        "Checking outputted in path format on mode MMDDYYYY",
    )


if __name__ == "__main__":
    log = Logger(initialize=False)
    log.initialize("dateTimeTest", 1000, "logs", Logger.DEFAULT_MASK)
    log.addEntry("Starting dateTime test suite", Logger.INFO_MASK)
    runTest()
    test.printResults()
