from calendar import monthrange, weekday
from datetime import date, timedelta, datetime

from config import Config

cfg = Config()


def str2date(s):
    return datetime.strptime(s, cfg.date_fmt).date()


def get_holidays():
    return {k: [str2date(t[0]) for t in v] for k, v in cfg.holidays.items()}


holidays = get_holidays()


def is_weekday(dt):
    return weekday(dt.year, dt.month, dt.day) in range(5)


def is_holiday(dt):
    return dt in holidays[dt.year]


def last_month_date(dt):
    yy, mm = dt.year, dt.month
    dd = monthrange(yy, mm)[1]
    return date(yy, mm, dd)


def first_month_date(dt):
    return date(dt.year, dt.month, 1)


def month_days(dt):
    return days_btw(first_month_date(dt), last_month_date(dt), True)


def days_btw(x, y, rincl=False):
    """Returns dates between the 2 given dates
    use rincl = True to include the last day as well (Right Inclusive)."""
    if x > y:
        return days_btw(y, x, rincl)
    while y - x > timedelta(0) or rincl and x == y:
        yield x
        x += timedelta(1)


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
