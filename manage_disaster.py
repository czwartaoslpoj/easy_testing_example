
from errors import InvalidDisasterNameError

class ManageDisaster:

    # def __init__(self, name, date):
    #     self.name = name
    #     self.date = date

    def report_disaster(self, name, date):
        if type(name) != str:
            raise InvalidDisasterNameError("Name of disaster needs to be of type: string")
        else:
            return f"Disaster occured! {name} on {date}. Let's wait for the next disaster to happen!"


    def check_if_disaster_happened_during_the_weekend(self, date):
        week_day = date.weekday()
        if week_day < 5:
            return "Disaster didn't occur during the weekend."
        else:
            return "Disaster occurred during the weekend! Again!"



