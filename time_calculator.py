import re


def add_time(start, duration, option=False):

    daysInWeek = list(['Monday', 'Tuesday', 'Wednesday',
                       'Thursday', 'Friday', 'Saturday', 'Sunday'])

    startHour = int(re.findall('\\d+', start)[0])
    startMinute = int(re.findall('\\d+', start)[1])
    startEnd = re.findall('AM|PM', start)[0]
    durationHour = int(re.findall('\\d+', duration)[0])
    durationMinute = int(re.findall('\\d+', duration)[1])

    countDayLater = 0
    startDay = str()
    returnString = str()

    for n in range(durationHour):
        if startHour == 11:
            if startEnd == 'PM':
                countDayLater += 1
                startEnd = 'AM'
            else:
                startEnd = 'PM'
        if startHour == 12:
            startHour = 1
        else:
            startHour += 1

    for n in range(durationMinute):
        if startMinute != 59:
            startMinute += 1
        else:
            startMinute = 0
            if startHour == 11:
                if startEnd == 'PM':
                    countDayLater += 1
                    startEnd = 'AM'
                else:
                    startEnd = 'PM'
            if startHour == 12:
                startHour = 1
            else:
                startHour += 1

    startHour = str(startHour)
    startMinute = str(
        startMinute) if startMinute >= 10 else '0' + str(startMinute)

    if option:
        for day in daysInWeek:
            if(re.search(option, day, re.IGNORECASE)):
                startDay = day
                break
        indexOfStartDay = daysInWeek.index(startDay)
        for n in range(countDayLater):
            if indexOfStartDay == 6:
                indexOfStartDay = 0
            else:
                indexOfStartDay += 1
        if countDayLater == 0:
            returnString = startHour + ':' + startMinute + ' ' + \
                startEnd + ', ' + daysInWeek[indexOfStartDay]
        elif countDayLater == 1:
            returnString = startHour + ':' + startMinute + ' ' + \
                startEnd + ', ' + daysInWeek[indexOfStartDay] + ' (next day)'
        else:
            returnString = startHour + ':' + startMinute + ' ' + \
                startEnd + ', ' + \
                daysInWeek[indexOfStartDay] + \
                ' (' + str(countDayLater) + ' days later)'

    else:
        if countDayLater == 0:
            returnString = startHour + ':' + \
                startMinute + ' ' + startEnd
        elif countDayLater == 1:
            returnString = startHour + ':' + \
                startMinute + ' ' + startEnd + ' (next day)'
        else:
            returnString = startHour + ':' + startMinute + ' ' + \
                startEnd + ' (' + str(countDayLater) + ' days later)'

    return returnString
