from multi_metric_pet import MultiMetricPet
from metric import Metric
from decorators import sync
import matplotlib.patches as mpatches

class AgingPet(MultiMetricPet):
    def __init__(self):
        super(AgingPet, self).__init__()
        self.metrics['age'] = Metric(value=0, update_period=2, update_rate= -1)
        self.young = range(20)
        self.old = range(20,40)
        self.stage = 'young'

    @sync
    def check_age(self):
        if self.metrics['age'].value in self.young:
            self.stage = 'young'
        elif self.metrics['age'].value in self.old:
            self.stage = 'old'
        else:
            self.dead = True

    @sync
    def show_age(self):
        if self.stage == 'young':
            age_patch = mpatches.Patch(color='olive', label='young')
        else:
            age_patch = mpatches.Patch(color='brown', label='old')
        self.leg.legendHandles.append(age_patch)
        self.leg.remove()
        self.ax.legend(handles=self.leg.legendHandles)
        self.fig.canvas.draw()

    def update_status(self):
        super(AgingPet,self).update_status()
        self.check_age()

    def show(self):
        super(AgingPet,self).show()
        self.show_age()



