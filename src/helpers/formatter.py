import datetime as dt
from datetime import date, timedelta


# confirm we are using a valid weekday and force to most recent if not
def get_most_recent_weekday():
    today = date.today()
    if today.isoweekday() == 6:
        start_date = date.today() - timedelta(days=1)
    elif today.isoweekday() == 7:
        start_date = date.today() - timedelta(days=2)
    else:
        start_date = date.today()
    return start_date


def get_threshold_color(threshold):
    if threshold <= 33:
        threshold_color = "red"
    elif 33 < threshold <= 67:
        threshold_color = "white"
    elif 67 < threshold <= 100:
        threshold_color = "white"
    else:
        threshold_color = "black"

    return threshold_color


def get_status_color(value):
    if value <= 33:
        status_color = "green"
    elif 33 < value <= 67:
        status_color = "orange"
    else:
        status_color = "red"

    return status_color


def get_my_name():
    print("Bob")
