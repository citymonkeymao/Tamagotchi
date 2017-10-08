import sys
import time
sys.path.append('../game')
from pet import BasicPet
from death_metric import DeathMetric
b = BasicPet()
b.metrics['hunger'] = DeathMetric(value = 0.1, update_period=1, update_rate=0.1)
for i in range(3):
    time.sleep(1)
    b.update_status()
    b.show()
print b.dead