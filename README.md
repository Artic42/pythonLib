# pythonLib

This is my personal general case python modules and apps to be used in other projects

## testEngine

Test engine is a simple module with the propose of running automated test, this allows to create test for the rest of the library easily.

## dateTime

Library to manage dates for other proposes.

Public methods for setting dates
* __setToNow__
* __setTo__ (year, month, day, hour, minute, second)
* __setToString__ (string)
* __setMode__ (mode)
    * _mode1_: YYYYMMDD
    * _mode2_: DDMMYYYY
    * _mode3_: MMDDYYYY

Public methods to get values from the object
* __getDate__
* __getTime__
* __getDateTime__
* __getYear__
* __getMonth__
* __getDay__
* __getHour__
* __getMinute__
* __getSecond__
* __getMode__

## Log

A simple log system