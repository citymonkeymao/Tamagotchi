import sys
import time
sys.path.append('../game')
from koala import Koala
from game_exceptions import PetDeadException
b = Koala()
b.feed()
try:
    for i in range(18):
        time.sleep(1)
        b.update_status()
        b.show()
    b.feed()
    for i in range(7):
        time.sleep(1)
        b.update_status()
        b.show()
    b.feed()
    for i in range(20):
        time.sleep(1)
        b.update_status()
        b.show()
    print 'putting the animal to bed at ' + str(b.metrics['daytime'].value)
    b.to_bed()
    for i in range(24):
        time.sleep(1)
        b.update_status()
        b.show()
    print 'putting the animal off bed at ' + str(b.metrics['daytime'].value)
    b.off_bed()
    b.feed()
    for i in range(24):
        time.sleep(1)
        b.update_status()
        b.show()
except PetDeadException as e:
    print 'PetDeadException occured'
    print e.message
