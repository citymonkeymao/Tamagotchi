import datetime
class BasicPet():
    #1 second as a time period
    _CLOCK_PERIOD = 1
    #update period, rate and time
    _HUNGER_UPDATE_PERIOD = 5
    _HUNGER_UPDATE_RATE = 0.2
    _HUNGER_LAST_UPDATED = 0
    def __init__(self):
        self.status_hunger = 1.0
        self._HUNGER_LAST_UPDATED = datetime.datetime.now()

