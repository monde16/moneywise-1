#!/usr/bin/env python
from calendar import monthrange, weekday
from datetime import datetime, date, time, timedelta
import argparse
import re


def get_args():
    """Initializes the arguments we want from the user.
    Returns the parsed arguments."""
    parser = argparse.ArgumentParser(description='Computes the number of working days between 2 given dates.')
    parser.add_argument('-f', '--first', help='the first date. If not given, datetime.now will be used', type=str)
    parser.add_argument('-l', '--last', help='the second (last) date. If not given, the end of month will be used', type=str)
    return parser.parse_args()


def str2date(s):
    if re.match(r'\d\d\d\d[^\d]\d\d?[^\d]\d\d?', s):
        t = tuple([int(e) for e in s.split(s[4])])
        return date(*t)
    else:
        raise ValueError(f'{s} is not of fomat: yyyy/mm/dd')


def is_weekday(date):
    return weekday(date.year, date.month, date.day) in range(5)


def last_month_date(dt):
    yy, mm = dt.year, dt.month
    dd = monthrange(yy, mm)[1]
    return date(yy, mm, dd)


def weekdays(a, b):
    """Calculate weekdays between dates a & b.

    The calc is right exclusive. Thus [a, b), much like range() and other similar methods
    """
    td = timedelta(1)
    n = 0
    while a + td*n < b:
        day = a + td * n
        n += 1
        if is_weekday(day):
            yield day


def main():
    args = get_args()
    
    first = str2date(args.first) if args.first else datetime.now().date()
    last = str2date(args.last) if args.last else last_month_date(first)
    days = len(list(weekdays(first, last + timedelta(1)))) # here we go past the last day so that the weekdays method includes it.
    print(f'{first} .. {last} => {days} week days')


if __name__ == '__main__':
    main()
