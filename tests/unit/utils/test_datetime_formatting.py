import datetime

import pytest

from vbm.utils.datetime_formatting import datetime_to_str


def test_datetime_to_str():
    dt = datetime.datetime(
        year=2019,
        month=3,
        day=28,
        hour=4,
        minute=20,
        second=42,
        microsecond=123,
    )

    expected_str = "03-28-2019T04:20:42"
    result_str = datetime_to_str(dt=dt)
    assert result_str == expected_str
