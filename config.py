year_18 = [
    ('2018-01-01', "New Year’s Day"),
    ('2018-03-21', "Human Rights Day"),
    ('2018-03-30', "Good Friday"),
    ('2018-04-02', "Family Day"),
    ('2018-04-27', "Freedom Day"),
    ('2018-04-30', "School Holiday"),
    ('2018-05-01', "Workers’ Day"),
    ('2018-06-16', "Youth Day"),
    ('2018-08-09', "National Women’s Day"),
    ('2018-08-10', "School Holiday"),
    ('2018-09-24', "Heritage Day"),
    ('2018-12-16', "Day of Reconciliation"),
    ('2018-12-17', "Public Holiday"),
    ('2018-12-25', "Christmas Day"),
    ('2018-12-26', "Day of Goodwill"),
]

# Source: https://www.officeholidays.com/countries/south_africa/index.php
year_19 = [
    ('2019-01-01', "New Year's Day"),
    ('2019-03-21', "Human Rights Day"),
    ('2019-04-19', "Good Friday"),
    ('2019-04-22', "Family Day"),
    ('2019-04-27', "Freedom Day"),
    ('2019-05-01', "Labour Day"),
    ('2019-06-16', "Youth Day"),
    ('2019-06-17', "Public Holiday"),
    ('2019-08-09', "National Women's Day"),
    ('2019-09-24', "Heritage Day"),
    ('2019-12-16', "Day of Reconciliation"),
    ('2019-12-25', "Christmas Day"),
    ('2019-12-26', "Day of Good Will"),
]

year_20 = [
    ('2020-01-01', "New Year's Day"),
    ('2020-03-21', "Human Rights Day"),
    ('2020-04-10', "Good Friday"),
    ('2020-04-13', "Family Day"),
    ('2020-04-27', "Freedom Day"),
    ('2020-05-01', "Workers' Day"),
    ('2020-06-16', "Youth Day"),
    ('2020-08-09', "National Women's Day"),
    ('2020-08-10', "National Women's Day (in lieu)"),
    ('2020-09-24', "Heritage Day"),
    ('2020-12-16', "Day of Reconciliation"),
    ('2020-12-25', "Christmas Day"),
    ('2020-12-26', "Day of Good Will"),
]


class Config(object):
    holidays = {
        2018: year_18,
        2019: year_19,
        2020: year_20
    }
    # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    date_fmt = '%Y-%m-%d'
