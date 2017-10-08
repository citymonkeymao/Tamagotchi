from metric import Metric


class DeathMetric(Metric):
    def update(self,pet):
        super(DeathMetric,self).update(pet)
        if self.value <= 0 :
            pet.dead = True
