import sys
sys.path.append('../game')
from game import show_status
from pet import *
import thread

b = BasicPet()
thread.start_new_thread(show_status,(b,))
while True:
    i = raw_input()
    exec(i)