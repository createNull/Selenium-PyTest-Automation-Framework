"""Testing data and functions that generate random testing data"""

from datetime import date, timedelta
from random import random
from time import mktime, localtime, strftime, strptime

URL = 'https://testertest.boltstaging.com/'
DATE_FORMAT = '%d %m %Y'

# Selectors
travel_time_hour = "travel_time_hour"
travel_time_minute = "travel_time_minute"

travel_date_day = "travel_date_day"
travel_date_month = "travel_date_month"
travel_date_year = "travel_date_year"

birth_date_day = "date_of_birth_day"
birth_date_month = "date_of_birth_month"
birth_date_year = "date_of_birth_year"

submit_btn = "input[type='submit']"

ticket_fare = "#price > strong"

error_message = ".errorlist > li"

# Errors
err_req_field = "This field is required."
err_invalid_date = "Enter a valid date."
err_earliest_day = "You cannot travel before tomorrow."
err_future_birth_day = "This date cannot be in the future."


def random_date(start: str, end: str) -> str:
    """Gives a random date in specified range.
    Function's parameters must use same date format."""

    start_time = mktime(strptime(start, DATE_FORMAT))
    end_time = mktime(strptime(end, DATE_FORMAT))
    random_time = start_time + random() * (end_time - start_time)

    return strftime(DATE_FORMAT, localtime(random_time))


def start_date(min_age: int) -> str:
    today = date.today()
    start_year = today.year - min_age
    return date(start_year, today.month, today.day).strftime(DATE_FORMAT)


def end_date(max_age: int) -> str:
    today = date.today()
    end_year = today.year - max_age
    return (date(end_year, today.month, today.day) - timedelta(days=1)).strftime(DATE_FORMAT)


def random_birth_date(category: str = None, age: int = None) -> str:
    """Generates a random birth date (day, month, year) depending on the age category or
    generates a random age based on a value.

    random_birth_date('young') => returns a random date of a person with age in range (0, 15)
    random_birth_date('adult') => returns a random date of a person with age in range (16, 59)
    random_birth_date('elder') => returns a random date of a person with age in range (60, 120)
    random_birth_date(age = 10) => returns a random date of a person born 10 years ago"""

    if age:
        start = start_date(age)
        end = end_date(age + 1)
    elif category == 'young':
        start = start_date(0)
        end = end_date(16)
    elif category == 'adult':
        start = start_date(16)
        end = end_date(60)
    elif category == 'elder':
        start = start_date(60)
        end = end_date(120)
    else:
        return 'Please provide an appropriate category or age'
    return random_date(start, end)


def days_from_now(days: int) -> str:
    """Generates a date considering the current day

    days_from_now(1) => returns date for tomorrow
    days_from_now(5) => returns date for 5 days from now"""

    today = date.today()
    return (date(today.year, today.month, today.day) + timedelta(days=days)).strftime(DATE_FORMAT)
