import datetime

from calendar import monthrange
from dateutil.relativedelta import relativedelta


def first_day(date):
    """月初を返す"""
    return datetime.date(date.year, date.month, 1)


def is_last_day(date):
    """月末日付ならTrueを返す"""
    return days_of_month(date.year, date.month) == date.day


def days_of_month(year, month):
    """年,月の日数を返す"""
    return monthrange(year, month)[1]


def last_day(date):
    """月末を返す"""
    return datetime.date(year=date.year, month=date.month, day=days_of_month(date.year, date.month))


def add_months(date, months):
    """月を加減する。
    dateにはdatetime.dateクラスのオブジェクト
    monthsには整数で月数を指定する。
    月末をOracleのadd_months互換の方法で処理する。
    例えば、
    2007年2月28日（月末）に1ヶ月足すと3月31日（月末）。
    2008年2月29日（月末）に1ヶ月足すと2008年3月31日（月末）。
    2008年2月28日（月末ではない）に1ヶ月足すと2008年3月28日（同じ日）。
    """
    if months == 0:
        return date

    if is_last_day(date):
        fst_date = first_day(date)
        lst_date = last_day(fst_date + relativedelta(months=months))
    else:
        lst_date = date + relativedelta(months=months)

    return lst_date
