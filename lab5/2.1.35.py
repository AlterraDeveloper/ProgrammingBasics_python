import datetime, calendar

def printCalendar(month, year):
    
    num_days = calendar.monthrange(year, month)[1]
    days = [datetime.date(year, month, day) for day in range(1, num_days+1)]

    months = {
     1: 'January',
     2: 'February',
     3: 'March',
     4: 'April',
     5: 'May',
     6: 'June',
     7: 'July',
     8: 'August',
     9: 'September',
     10: 'October',
     11: 'November',
     12: 'December'
    }

    weekDays = {
     0: 'Sun',
     1: 'Mon',
     2: 'Tue',
     3: 'Wed',
     4: 'Thu',
     5: 'Fri',
     6: 'Sat'
    }

    additionalFillings = 0
    if ((7 - (7 - (days[0].weekday() + 1))) != 7):
        additionalFillings = (7 - (7 - (days[0].weekday() + 1)))

    numOfRows = (additionalFillings + len(days)) / 7
    if (int(numOfRows) != numOfRows):
        numOfRows = int(numOfRows) + 1
    else:
        numOfRows = int(numOfRows)
        
    dayCount = 0
    dayNum = 1
    print('        ' + str(months[month]) + ' ' + str(year))
    for row in range(0, numOfRows + 1):
        for col in range(0, 7):
            if (row == 0):
                print(weekDays[col], end=' ')
            else:
                if (dayCount >= additionalFillings and dayNum <= len(days)):
                    print('{0: 3d}'.format(dayNum), end=' ')
                    dayNum += 1
                else:
                    print('   ', end=' ')
                dayCount += 1
        print()

month = int(input('Введите номер месяца: '))
year = int(input('Введите год: '))

printCalendar(month, year)