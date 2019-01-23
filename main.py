from strategy import SimpleStrategy
from utils import *

MAX_HRS = 88


def main():
    print(f"On month: {date.today()}")

    st = SimpleStrategy([{'id': i, 'hrs': 0, 'wkc': 0, 'otc': 0} for i in range(1, 13)])
    print(f"People = {st}")

    for d in month_days(date.today()):
        pair = st.nxt()
        assign_pair(pair[0], pair[1], d)
        print(f'[dbg] {d}, {day_of_week(d)}')
        print(st)

    print(st)


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
            hrs_to_work = 24
        else:
            hrs_to_work = 7
        hrs_to_work = min(hrs_to_work, MAX_HRS-p['hrs'])
        p['hrs'] += hrs_to_work
        if hrs_to_work > 7 or is_weekend(d):
            p['otc'] += 1
        return hrs_to_work > 0
    else:
        return False


if __name__ == '__main__':
    main()
