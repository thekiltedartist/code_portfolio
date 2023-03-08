import math
import dice_bag as dice


# need to add attack, random HP, random AC
class Character:
    def __init__(self, name, **kwargs):
        self.name = name
        self.score = kwargs
        self.stats = {}
        self.hp = 23

    def mod(self):
        # see if it is possible store score and mod withing in a list withing the dictionary, executing a funtion
        # that generates the bonus
        stats = {}
        for stat, score in self.score.items():
            bonus = math.floor((score - 10) / 2)
            stats[stat] = [score, bonus]
        self.stats = stats

    def bab(self):
        pass


# add npc name, health, stats, attack, ac, and
class NPC(Character):
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        self.hp = 0
        self.dc = 0

    def npc_hp(self):
        self.hp = dice.d6() + dice.d6(6)

    def _npc_dc(self):
        self.dc = dice.d20(7)


# see if it is possible store score and mod withing in a list withing the dictionary,
# executing a function that generates the bonus

