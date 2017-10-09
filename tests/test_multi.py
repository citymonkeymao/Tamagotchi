import sys
import time
sys.path.append('../game')
from multi_metric_pet import MultiMetricPet
from game_exceptions import PetDeadException
b = MultiMetricPet()
b.feed()
try:
    for i in range(10):
        time.sleep(1)
        b.update_status()
        b.show()
    b.feed()
    b.clean()
    b.play()
    for i in range(5):
        time.sleep(1)
        b.update_status()
        b.show()
    b.feed()
    for i in range(20):
        time.sleep(1)
        b.update_status()
        b.show()

except PetDeadException as e:
    print 'PetDeadException occured'
    print e.message

input('game over')