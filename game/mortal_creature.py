from pet import BasicPet
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from death_metric import DeathMetric

class PetDeadException(Exception):
    def __init__(self, message, errors):
        # Call the base class constructor with the parameters it needs
        super(BaseException, self).__init__(message)

        # Now for your custom code...
        self.errors = errors

class MortalCreature(BasicPet):
    def __init__(self):
        self.dead = False
        self.metrics = dict()
        self.metrics['hunger'] = DeathMetric(update_period=1, update_rate=0.02)

    def update_status(self):
        if self.dead:
            raise PetDeadException('updating dead animal',1)
        else:
            super(MortalCreature, self).update_status()

    def feed(self):
        if self.dead:
            raise PetDeadException('feeding dead animal',1)
        else:
            super(MortalCreature, self).update_status()

    def show(self):
        if self.dead:
            im = mpimg.imread('../resources/dead.jpg')
            plt.imshow(im)
        else:
            super(MortalCreature, self).show()