import sys
import time
sys.path.append('../game')
from pet import BasicPet
b = BasicPet()
for i in range(10):
    time.sleep(1)
    b.update_status()
    b.show()
b.feed()
b.show()
input("Press [enter] to continue.")