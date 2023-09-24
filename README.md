# pythonLib

This is my personal general case python modules and apps to be used in other projects

## testEngine

Test engine is a simple module with the propose of running automated test, this allows to create test for the rest of the library easily. Test are separated in scenario, once a test in a scenario fail the rest of the scenario is skipped. It also outputs using colored test with errors in red and pass test in green. It has the following methods:
* testIfEqual
* testIfFalse
* testIfEqual
* testIfNotEqual
* ...

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
* __getDateTimePathFomat__ (It prints the date and time in a format usable in paths, for files)

## Log

A simple log system, it creates a log iwth 7 mask levels and a maximun size of file. If you log more lines than max it creates a new log file. Available masks

* INFO_MASK
* WARN_MASK
* ERROR_MASK
* COMMS_SEND_MASK
* COMMS_RECV_MASK
* HERMES_MASK000
* COMMS_MASK
* DEBUG_MASK
