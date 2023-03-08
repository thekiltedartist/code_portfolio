from character import Character, NPC
from char_stats import hendricks, generic_npc
import dice_bag as dice

hero = Character("Hendricks",**hendricks)
hero.mod()

baddy_1 = NPC("Thug", **generic_npc)
baddy_1.mod()
baddy_1.npc_hp()

print(hero.stats)
print(baddy_1.stats)
print(baddy_1.hp)



