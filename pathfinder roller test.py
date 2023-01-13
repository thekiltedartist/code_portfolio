def roll_d20(x):
    import random
    d20_roll = random.randint(1,20)
    return d20_roll + x

def roll_d6 (y):
    import random
    d6_roll = random.randint(1,6)
    return d6_roll + y

npc_ac = 18

attack_mod = int(input("What is your attack modifier? "))
damage_mod = int(input("What is your damage modifier? "))
player_attack = roll_d20(attack_mod)
crit_check = player_attack - attack_mod


if crit_check == 20:
    print("Critical Threat!")
    if roll_d20(attack_mod) >= npc_ac:
            print(f" Confirmed Critical! {roll_d6(damage_mod)*2} points of damage!")
elif crit_check == 1:
    print("Critical FUMBLE!")
elif player_attack >= npc_ac:
    print(f'You did {roll_d6(damage_mod)} against the enemy!')
else:
    print(f"{player_attack}. Miss!")
