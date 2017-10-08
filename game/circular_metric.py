from metric import Metric

class CircleMetric(Metric):
    def __init__(self, value = 0, update_period = 1, update_rate = 1, maximum = 24):
        super(CircleMetric,self).__init__(value,update_period,update_rate)
        self.maximum = maximum
    def update(self,pet):
        super(CircleMetric,self).update()
        self.value %= self.maximum