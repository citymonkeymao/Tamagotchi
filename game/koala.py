from mortal_creature import MortalCreature
from death_metric import DeathMetric



class sleepy_pet(MortalCreature):
    def __init__(self):
        self.dead = False
        self.metrics = dict()
        self.metrics['hunger'] = DeathMetric(update_period=1, update_rate=0.1)