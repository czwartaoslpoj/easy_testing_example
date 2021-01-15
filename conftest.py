import pytest
from manage_disaster import ManageDisaster
import datetime
import arrow


@pytest.fixture(scope="module")
def disaster():
    disaster = ManageDisaster()
    return disaster


@pytest.fixture(scope="class")
def date():
    date = datetime.date(2021, 1, 14)
    return date

# @pytest.fixture(scope="class")
# def name():
#     name = "Overslept for stand-up"
#     return name