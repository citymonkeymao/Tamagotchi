import sys
sys.path.append('../game')
from game import start_play
import time
from pet import *
import thread
b = BasicPet()

#use a new thread to feed
def feed():
    time.sleep(5)
    b.feed()
thread.start_new_thread(feed,())

start_play(b)

