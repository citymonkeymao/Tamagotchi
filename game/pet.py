from metric import Metric
import matplotlib.pyplot as plt
from decorators import sync
class BasicPet(object):
    def __init__(self):
        self.metrics = dict()
        self.metrics['hunger'] = Metric(update_period=1, update_rate=0.02)


    @sync
    def update_status(self):
        #update all matics
        map(lambda m: self.metrics[m].update(self), self.metrics)
    @sync
    def feed(self):
        self.metrics['hunger'].inc(0.5)
    @sync
    def show(self):
        if not hasattr(self, 'fig'):
            plt.ion()
            plt.show()
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(111)
        if hasattr(self,'bar'):
            self.bar.remove()
        values = map(lambda m: m.value, self.metrics.values())
        self.bar = self.ax.bar(range(self.metrics.__len__()), values,color='b',tick_label=self.metrics.keys())
        self.fig.canvas.draw()
