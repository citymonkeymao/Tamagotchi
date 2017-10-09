from koala import Koala
from metric import Metric
from death_metric import DeathMetric
from decorators import sync, sleep_check,death_check

class MultiMetricPet(Koala):
    def __init__(self):
        super(MultiMetricPet,self).__init__()
        self.sleep_after = 18
        self.metrics['happiness'] = Metric(value=20, update_period=2, update_rate=0.5)
        self.metrics['health'] = DeathMetric(value=10, update_period=1,update_rate=0.5)

    @sleep_check
    @death_check
    @sync
    def play(self):
        self.metrics['happiness'].inc(5)

    @sleep_check
    @death_check
    @sync
    def clean(self):
        self.metrics['health'].inc(5)