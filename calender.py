import calendar

def calendar_display():

    year = int(input('Enter the year: '))
    month = int(input('Enter the month (1-12):'))

    cal = calendar.TextCalendar(calendar.SUNDAY)

    calendar_month = cal.formatmonth(year, month)
    print(calendar_month)

calendar_display()