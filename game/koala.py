from mortal_creature import MortalCreature
from death_metric import DeathMetric
from circular_metric import CircularMetric
import matplotlib.patches as mpatches
from decorators import sync, death_check, sleep_check

class Koala(MortalCreature):
    def __init__(self):
        self.dead = False
        self.sleep = True
        self.on_bed = False
        self.sleep_after = 6
        self.metrics = dict()
        self.metrics['hunger'] = DeathMetric(value=25, update_period=1, update_rate=0.2)
        self.metrics['daytime'] = CircularMetric()
    def update_status(self):
        super(Koala,self).update_status()
        if self.metrics['daytime'].value > self.sleep_after or self.on_bed:
            self.sleep = True
        else:
            self.sleep = False

    @death_check
    @sleep_check
    @sync
    def to_bed(self):
        self.on_bed = True

    @death_check
    @sync
    def off_bed(self):
        self.on_bed = False

    @death_check
    @sleep_check
    @sync
    def feed(self):
        self.metrics['hunger'].inc(5)



    @sync
    def show(self):
        #show sleep and bed status
        super(Koala,self).show()
        if hasattr(self,'leg'):
            self.leg.remove()
         
        if self.sleep:
            sleep_patch = mpatches.Patch(color='red', label='sleeping')
        else:
            sleep_patch = mpatches.Patch(color='white', label='awake')

        if self.on_bed:
            bed_patch = mpatches.Patch(color='yellow', label='on bed')
        else:
            bed_patch = mpatches.Patch(color='green', label='off bed')

        self.leg = self.ax.legend(handles = [sleep_patch,bed_patch])
        self.fig.canvas.draw()