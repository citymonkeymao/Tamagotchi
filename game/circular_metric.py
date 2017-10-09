from metric import Metric

class CircularMetric(Metric):
    def __init__(self, value = 0, update_period = 1, update_rate = 1, maximum = 24):
        super(CircularMetric, self).__init__(value, update_period, update_rate)
        self.maximum = maximum
    def update(self,pet):
        super(CircularMetric, self).update(pet)
        self.value %= self.maximum