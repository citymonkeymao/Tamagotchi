import sys
import time
sys.path.append('../game')
from aging_pet import AgingPet
from game_exceptions import PetDeadException
b = AgingPet()
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
    b.feed()
    b.clean()
    b.play()
    for i in range(20):
        time.sleep(1)
        b.update_status()
        b.show()
    b.feed()
    b.clean()
    b.clean()
    b.play()
    for i in range(24):
        time.sleep(1)
        b.update_status()
        b.show()
    b.feed()
    b.clean()
    b.clean()
    b.clean()
    b.clean()
    b.play()
    for i in range(24):
        time.sleep(1)
        b.update_status()
        b.show()
    b.feed()

except PetDeadException as e:
    print 'PetDeadException occured'
    print e.message

input('game over')