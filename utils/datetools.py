import pytz
from datetime import date, datetime
from dateutil.relativedelta import relativedelta


def calculate_age(start_date, end_date):
    return relativedelta(end_date, start_date)


def calculate_pet_age(birth_date, today):
    birth_date = first_of_month(
        is_datetime=True).replace(year=birth_date.year, month=birth_date.month)
    return calculate_age(birth_date, today)


def utc_now() -> datetime:
    return pytz.UTC.localize(datetime.utcnow())


def utc_date() -> date:
    return utc_now().date()


def first_of_month(is_datetime: bool = False) -> datetime | date:
    utc_date_func = utc_now if is_datetime else utc_date
    return utc_date_func().replace(day=1)
