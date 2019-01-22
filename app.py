#!/usr/bin/env python
import argparse
from datetime import datetime

from utils import *


def get_args():
    """Initializes the arguments we want from the user.
    Returns the parsed arguments."""
    parser = argparse.ArgumentParser(description='Computes the number of working days between 2 given dates.')
    parser.add_argument('-f', '--first', help='the first date. If not given, datetime.now will be used', type=str)
    parser.add_argument('-l', '--last', help='the second (last) date. If not given, the end of month will be used', type=str)
    return parser.parse_args()


def main():
    args = get_args()

    first = str2date(args.first) if args.first else datetime.now().date()
    last = str2date(args.last) if args.last else last_month_date(first)
    days = len(list(workdays(first, last + timedelta(1)))) # here we go past the last day so that the workdays method includes it.
    print(f'{first} .. {last} => {days} work days')


if __name__ == '__main__':
    main()
