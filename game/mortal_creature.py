from pet import BasicPet
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from death_metric import DeathMetric
from decorators import death_check

class MortalCreature(BasicPet):
    def __init__(self):
        self.dead = False
        self.metrics = dict()
        self.metrics['hunger'] = DeathMetric(update_period=1, update_rate=0.1)

    @death_check
    def update_status(self):
        # if self.dead:
        #     raise PetDeadException('updating dead animal',1)
        # else:
        super(MortalCreature, self).update_status()

    @death_check
    def feed(self):
        # if self.dead:
        #     raise PetDeadException('feeding dead animal',1)
        # else:
        super(MortalCreature, self).feed()

    def show(self):
        if self.dead:
            im = mpimg.imread('../resources/dead.jpg')
            if hasattr(self,'fig'):
                self.ax.clear()
                self.ax.imshow(im)
                self.ax.set_xticks([0])
                self.ax.set_xticklabels(['Your pet dead'])
                self.fig.canvas.draw()
            else:
                plt.imshow(im)
                plt.xticks(['Your pet dead'])
        else:
            super(MortalCreature, self).show()