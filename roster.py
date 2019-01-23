#!/usr/bin/env python
import argparse
from datetime import datetime
import logging as log

from strategy import SimpleStrategy
from utils import *

MAX_HRS = 88
OT_HRS = 24
NORM_HRS = 7


def proc(fst, lst):
    log.info(f'From: {fst}, To: {lst}')
    st = SimpleStrategy([{'id': i, 'hrs': 0, 'wkc': 0, 'otc': 0} for i in range(1, 13)])
    log.debug(f"People = {st}")

    for d in days_btw(fst, lst, rincl=True):
        pair = st.nxt()
        assign_pair(pair[0], pair[1], d)
        log.debug(f'{d}, {day_of_week(d)}')
        log.debug(st)

    log.info("Done!")
    log.info(st)


def assign_pair(a, b, day):
    if is_weekday(day):
        a_ot, b_ot = True, False
    else:
        a_ot, b_ot = True, True

    assign(a, a_ot, day)
    assign(b, b_ot, day)


def assign(p, ot, d):
    p['wkc'] += 1
    hrs = p['hrs']
    if hrs < MAX_HRS:
        if ot:
            hrs_to_work = OT_HRS
        else:
            hrs_to_work = NORM_HRS
        hrs_to_work = min(hrs_to_work, MAX_HRS-p['hrs'])
        p['hrs'] += hrs_to_work
        if hrs_to_work > NORM_HRS or is_weekend(d):
            p['otc'] += 1
        return hrs_to_work > 0
    else:
        return False


def get_args():
    """Initializes the arguments we want from the user.
    Returns the parsed arguments."""
    parser = argparse.ArgumentParser(description='Computes the number of working days between 2 given dates.')
    parser.add_argument('-f', '--first', help='the first date. If not given, datetime.now will be used', type=str)
    parser.add_argument('-l', '--last', help='the second (last) date. If not given, the end of month will be used', type=str)
    return parser.parse_args()


def main():
    log.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=log.INFO, datefmt='%Y-%m-%d %I:%M:%S %p')

    args = get_args()

    first = str2date(args.first) if args.first else datetime.now().date()
    last = str2date(args.last) if args.last else last_month_date(first)

    proc(first, last)


if __name__ == '__main__':
    main()
