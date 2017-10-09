from pet import *
from mortal_creature import MortalCreature
from koala import Koala
from multi_metric_pet import MultiMetricPet
from aging_pet import AgingPet
import thread
import time
from IPython import embed

def show_status(animal):
    while True:
        time.sleep(1)
        animal.update_status()
        animal.show()


def start_play(animal):
    try:
        thread.start_new_thread(show_status,(animal,))
    except Exception as e:
        print "error when creating thread " + e.message
        exit(1)



if __name__ == '__main__':
    embed()
