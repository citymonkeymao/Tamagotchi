import sys
import time
sys.path.append('../game')
from mortal_creature import MortalCreature, PetDeadException
b = MortalCreature()
for i in range(5):
    time.sleep(1)
    b.update_status()
    b.show()
b.feed()
try:
    for i in range(12):
        time.sleep(1)
        b.update_status()
        b.show()
except PetDeadException as e:
    print 'PetDeadException occured'
    print e.message

print b.dead

try:
    b.feed()
except PetDeadException as e:
    print 'PetDeadException occured'
    print e.message

input("Press [enter] to continue.")