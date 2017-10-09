import datetime
import math
class Metric(object):
    def __init__(self, value = 1, update_period = 5, update_rate = 0.2):
        self.update_period = update_period
        self.value = value
        self.update_rate = update_rate
        self.last_updated = datetime.datetime.now()
    def update(self,pet):
        now = datetime.datetime.now()
        time_past = (now - self.last_updated).total_seconds()
        if time_past > self.update_period:
            self.value -= self.update_rate * math.floor(time_past / self.update_period)
            self.last_updated = now
    def inc(self, step):
        self.value += step

