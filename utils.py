import re
from calendar import monthrange, weekday
from datetime import date, timedelta

import config


def str2date(s):
    if re.match(r'(?:\d{4}([^\d])\d\d?\1\d\d?)', s):
        t = tuple([int(e) for e in s.split(s[4])])
        return date(*t)
    else:
        raise ValueError(f'{s} is not of fomat: yyyy/mm/dd')


def get_holidays():
    return [str2date(t[0]) for t in config.holidays]


holidays = get_holidays()


def is_weekday(date):
    return weekday(date.year, date.month, date.day) in range(5)


def is_holiday(date):
    return date in holidays


def last_month_date(dt):
    yy, mm = dt.year, dt.month
    dd = monthrange(yy, mm)[1]
    return date(yy, mm, dd)


def workdays(a, b):
    """Calculate workdays between dates a & b.

    The calc is right exclusive. Thus [a, b), much like range() and other similar methods
    """
    td = timedelta(1)
    n = 0
    while a + td*n < b:
        day = a + td * n
        n += 1
        if is_weekday(day) and not is_holiday(day):
            yield day


