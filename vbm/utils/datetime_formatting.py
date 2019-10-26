import datetime


_DATETIME_FORMAT = "%m-%d-%YT%H:%M:%S"


def datetime_to_str(dt: datetime.datetime) -> str:
    return dt.strftime(_DATETIME_FORMAT)
