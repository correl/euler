class Day:
    SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY = range(7)

def is_leap_year(year):
    return (year % 100 > 0 and year % 4 == 0) or (year % 400 == 0)

year = 1900
# 1/1/1900 was a Monday
first_day = Day.MONDAY

total = 0
while year < 2000:
    year = year + 1
    # Count last year's days to advance the starting weekday
    days = 366 if is_leap_year(year - 1) else 365
    # List the number of days in each month for this year
    months = [
        31,
        29 if is_leap_year(year) else 28,
        31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    ]
    first_day = (first_day + days % 7) % 7
    sundays = 0
    for m in range(len(months)):
        days = sum(months[:m])
        first_sunday = (7 - ((first_day + days % 7) % 7)) % 7 + 1
        if first_sunday == 1:
            total = total + 1

print 'Total months beginning on Sunday from 1/1/1901 to 12/31/2000: {0}'.format(total)
