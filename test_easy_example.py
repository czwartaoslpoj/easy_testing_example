import pytest
from errors import InvalidDisasterNameError
import datetime

def test_report_disaster(disaster, date):
    name_of_disaster = "Broken coffee machine"
    desired_result = "Disaster occured! Broken coffee machine on 2021-01-14. Let's wait for the next disaster to happen!"
    actual_result = disaster.report_disaster(name = name_of_disaster, date = date)
    assert desired_result == actual_result
    assert isinstance(actual_result, str)

def test_raising_invalid_disaster_name_error(disaster, date):
    name_of_disaster = 3
    with pytest.raises(InvalidDisasterNameError) as err:
        assert disaster.report_disaster(name_of_disaster, date)
    expected_message = "Name of disaster needs to be of type: string"
    assert expected_message == err.value.message

def test_check_if_disaster_happened_during_the_weekend(disaster, date):
    desired_result = "Disaster didn't occur during the weekend."
    actual_result = disaster.check_if_disaster_happened_during_the_weekend(date)
    assert desired_result == actual_result

# #peremetrizing
@pytest.mark.parametrize('date, result',
                         [
                             (datetime.date(2021, 1, 8), "Disaster didn't occur during the weekend."),
                             (datetime.date(2021, 1, 9), "Disaster occurred during the weekend! Again!"),
                             (datetime.date(2021, 1, 11), "Disaster didn't occur during the weekend.")
                         ]
                         )
def test_check_if_disaster_happened_during_the_weekend(disaster, date, result):
    assert disaster.check_if_disaster_happened_during_the_weekend(date) == result